# Youtube-Spam-Comment-Detector
Youtube Spam Comment Detector using ML. &amp; Flask


### Abstract
We know that YouTube has emerged as the most popular website for sharing and watching 
video content. However, such success has also attracted malicious users, whose goal is to self-promote their videos or spread viruses and malware. Therefore, it is very important to find ways to identify and report these videos & comments.
### Objective
The objective of this project is to create a web-app using python(Flask). This project will be build 
using python modules like Numpy, Flask, SkLearn, Mathplotlib... etc.
In this project, the user has to give youtube comment “predict” button. It will show the result 
below. If the user clicks on the “reload” button, then it will reload the app.
### Prerequisites
 1.Familiarity with Python
 2.Working knowledge of Random Forest algorithm and Bag of words model will be a plus.


To build this project we will use the basic concept of python and libraries

A)NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical 
functions to operate on these

B) pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for 
manipulating numerical tables and time series.

C) Flask is a micro web framework written in Python. It is classified as a microframework because 
it does not require particular tools or libraries. It has no database abstraction layer, form 
validation, or any other components where pre-existing third-party libraries provide common 
functions

D) Scikit-learn is a free software machine learning library for the Python programming language. 
It features various classification, regression and clustering algorithms including support vector 
machines, ...etc.

E) Matplotlib is a plotting library for the Python programming language and its numerical 
mathematics extension NumPy. It provides an object-oriented API for embedding plots into 
applications using general-purpose GUI toolkits like Tkinter, wxPython


To install the libraries we can use pip installer from the command line:
  1) pip install numpy
  2) pip install pandas
  3) pip install flask
  4) pip install sklearn
  5) pip install matplotlib
  
  or Open CMD in project Directory and type -
  
  pip install -r requirements.txt
  
###### Examples
![image](https://user-images.githubusercontent.com/60839928/129749027-c5b332d8-b873-42e4-b2db-bd2da7ddc24f.png)

### THE DATA SET
The dataset is pretty straightforward, it contains 2,000+ comments from popular Youtube videos, The dataset is formatted in a way where each row has a comment followed by a value marked as 1 or 0 for spam or not spam,
The dataset can be downloaded from this website --
https://www.kaggle.com/goneee/youtube-spam-classifiedcomments

#### Project Structure:
Let’s check the steps to build This project using Python
•	Import modules dataset
•	Preprocessing
•	Feature Selection
•	Feature Extraction and Feature Engineering
•	Analyzer and apply algorithm
•	Model Building
•	Predict & Output
##### Implemented Software: 
	Language: Python 3.9.
	IDE: Visual Studio Code 2021. 
	Jupyter Note Book / Google-Colab
	
#### System Diagram

![image](https://user-images.githubusercontent.com/60839928/129749793-5ed8260e-0962-405f-a013-e779e95b5d7b.png)

#### Algorithm (naive bayes)

![image](https://user-images.githubusercontent.com/60839928/129827928-799c790d-c78a-42ee-bbcf-7db882a2a4ef.png)


### Output

To Run this Application Open CMD in project Directory
	And Type This command: Python (filename.py)
	
For Example:
CMD-	Python app.py

* Running on http://127.0.0.1:8081/ (Press CTRL+C to quit)
So The Apploication is runing on localhost 8081 port. We can simplly check it  in our browser.

##### Home Page

![image](https://user-images.githubusercontent.com/60839928/129750610-fe2f1842-69ac-46e0-a120-bb7bc96d6ac9.png)

##### Not Spam Comment

![image](https://user-images.githubusercontent.com/60839928/129750660-84e871fe-52e0-4adb-8c11-be4ce2d9a75a.png)

##### Spam Comment

![image](https://user-images.githubusercontent.com/60839928/129750719-e5d825ac-4d82-4c60-a539-337078e4cdef.png)

### Debugging

##### When Application is Running...
![image](https://user-images.githubusercontent.com/60839928/129750846-065fc79e-e42d-4fea-9ae6-9345cc7ec549.png)

(Press CTRL+C to quit)

##### After Exit Application...

![image](https://user-images.githubusercontent.com/60839928/129750945-904277ef-7c07-4988-a606-773d0a29a041.png)

#### Application Source Code: 

Google-Colab link: 
https://colab.research.google.com/drive/1XDhr1U2d7AHjV9vgrsBsstuIrGMKDajL?authuser=1

#### Challenges Faced:
Faced error Dataset. Faced problem in Algorithms and Some Little bugs.

#### Outcome
The outcome of this project is a simple application all people can use to check spam comments.

### Conclusion:
This was a great experience doing this project. With these steps, I have successfully created a ML Project. For classifying the YouTube comments as spam and not spam (ham) there are various techniques used. This approach has been tested with real-time YouTube comments and given an overall outcome which is 92% accurate. This approach has been tested with real-time YouTube comments and given an overall outcome which is more accurate. I used popular libraries to rendering datasets and also learned about basics of Machine learning. In this way, I successfully created my youtube spam comment detector python project. The challenges I faced and the learning that will come in great help in the future. Hope you enjoyed it.

Thank You. 😊



