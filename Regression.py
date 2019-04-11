# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:58:01 2019

@author: SakthivelSundaram
"""

import pandas as pa
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


data = pa.read_excel("data.xls")

xy=data[data["TL"] >= 0]


features =["X1","X2","X3","X4","X5","X6"]

x=xy[features]

target =["Y1","Y2"]

y=xy[target]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.10 , random_state = 50)


regression =LinearRegression()  
dtr=regression.fit(x_train,y_train)

print("R Square ----->",dtr.score(x_train,y_train))

coef=(dtr.coef_)

print("coef>>>>",coef)

intercept = dtr.intercept_

print("intercept>>>>>",intercept)

prediction = dtr.predict(x_test)

print(prediction[:5])

print(y_test[:5])






