# -*- coding: utf-8 -*-
"""FilnalProj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19xmG_Udy9cpubS7IDb0GVeo_7zX1lH5s
"""

from google.colab import drive
drive.mount('/content/drive')

#Required libraries

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import confusion_matrix,classification_report

#Read the required files

file = pd.read_excel('drive/MyDrive/Colab Notebooks/digikala_raw(1).xlsx')
with open('drive/MyDrive/Colab Notebooks/Stopwords.txt', 'r', encoding="utf8") as file1:
  stopwords = file1.read().split('\n')

with open('drive/MyDrive/Colab Notebooks/Removepuncs.txt', 'r', encoding="utf8") as file2:
  removepuncs = file2.read().split('\n')

#Prepare Excel and delete cells that are not needed

file.drop(file.columns.difference(['comment', 'recommend', 'verification_status', 'title_en']), 1, inplace=True)
file.drop(file.index[file['title_en'] == 'HW'], inplace = True)
file.drop(file.index[file['title_en'] == 'PC'], inplace = True)
file.drop(file.index[file['title_en'] == 'TC'], inplace = True)
file.drop(file.index[file['title_en'] == 'FA'], inplace = True)
file.drop(file.index[file['title_en'] == 'PA'], inplace = True)
file.drop(file.index[file['title_en'] == 'MA'], inplace = True)
file.drop(file.index[file['title_en'] == 'TS'], inplace = True)
file.drop(file.index[file['title_en'] == 'HA'], inplace = True)
file.drop(file.index[file['verification_status'] == 'rejected'], inplace = True)
file = file[file['recommend'].isin(['recommended', 'no_idea', 'not_recommended'])]

#Remove redundant words

dataset = file.iloc[:, :].values
comments = []
recommend = []

for x in range(len(dataset)):
    comments.append(dataset[x][3])
    recommend.append(dataset[x][2])

for i in range(len(comments)):
  string = str(comments[i])

  for removepunc in removepuncs:
    string = string.replace(removepunc, ' ')

  string = [s for s in string.split(' ') if not s in stopwords]
  string = ' '.join(string)

  comments[i] = string

le = LabelEncoder()
recommend = le.fit_transform(recommend)

cv = CountVectorizer()
commentsarray = cv.fit_transform(comments).toarray()

#Divide the data into two parts: training and testing

train_x, test_x, train_y, test_y = train_test_split(commentsarray, recommend, test_size = 0.10, random_state = 0)
X_train = train_x
X_test = test_x
y_train = train_y
y_test = test_y

#Neural network training

lr = LogisticRegression()
lr.fit(X_train,y_train)
predictions = lr.predict(X_test)

#Confusion Matrix

new = np.asarray(y_test)
confusion_matrix(predictions,y_test)
new = np.asarray(y_test)
confusion_matrix(predictions,y_test)
print(classification_report(predictions,y_test))