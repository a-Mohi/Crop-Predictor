#Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import pickle

#Reading the dataset
dataset = pd.read_csv('Crop_recommendation.csv')

#Splitting x and y
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

#Apply Normalization
ss = StandardScaler()
X = ss.fit_transform(X)

#Apply LabelEncoder to Y
le = LabelEncoder()
Y = le.fit_transform(Y)

#Splitting the dataset into training and testing sets
x_train,x_test, y_train,y_test = train_test_split(X,Y,test_size=0.25, random_state=42)

#Apply XGBClassifier
xg = XGBClassifier()
xg.fit(x_train,y_train)

#Predicting the results
print(classification_report(xg.predict(x_test),y_test))

with open("model.pkl","wb") as f:
    pickle.dump(xg,f)