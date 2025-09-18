#importing necessary modules or libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#loading the required dataset
data = pd.read_csv('E:\\mini project 4th sem')
print(data.head())
#plotting the graph
figure = px.scatter(data, x="Salary",y="experience")
figure.show()
#importing sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#training and testing the dataset
x = np.asanyarray(data[["experience"]])
y = np.asanyarray(data[["Salary"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(xtrain, ytrain)
#input function
a = int(input("Years of Experience : "))
b=int(input("enter interview score:"))
features = np.array([[a]])
print("Predicted Salary = ", model.predict(features))

