#Flask Packages
from flask import Flask,render_template,url_for,request
from flask import *

# EDA Packages
import pandas as pd
import numpy as np

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 

app = Flask(__name__)

#Home
@app.route('/')
def home():
    #return "hello World"
    return render_template("youtubechk.html")

#PREDICTION 
@app.route('/ypredict',methods = ['POST'])
def predict():

    # Link to dataset from repo
    url = "data\YoutubeSpamMergedData.csv"
    #Read csv file
    df = pd.read_csv(url)
    # Data Framing
    df_data = df[["CONTENT","CLASS"]]
    # Featuers and Labels
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS

    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus) # fit the data

    # Training
    X_train,X_test,y_train,y_test = train_test_split(X,df_y,test_size=0.33,random_state = 42)

    #naive Bayes Classifire
    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    clf.score(X_test,y_test)

    # Accuracy
    print(f"Accuracy of model = {clf.score(X_test,y_test)*100} %")

    # getting request and sending respone
    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        print(f"Recived Comment  : {comment}")
        #DATA TRANSFORMING FOE PREDCTION
        vect = cv.transform(data).toarray()
        #PREDICT DATA IF 0 = NOT SPAM AND 1 = SPAM
        my_prediction = clf.predict(vect)
        print(f"Pridection :- {my_prediction} ")
        #RETURNING RESULT
        return render_template('youtubechk.html',prediction = my_prediction,comment = comment)



# Main Program Run from here
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8081, debug=True)




