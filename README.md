# Linear-Regression-Analysis-Using-Python
Linear Regression Analysis

# Simple Linear Regression 

Simple linear regression analysis deals with the single dependent and single independent variable following the below equation 

  y = ax +b 
  
  a = co-efficient of x 
  b = y intercept (error correction) 
  
  value of a and b can be calculated as 
       
                      (∑y)(∑X^2) – (∑(x)∑(xy))
        a =          ____________________            where N is the No. of Observations
                       N(∑(x^2)) – (∑(x))^2
                       
        
        
       
                         N(∑xy) – (∑(x)∑(y))
       b =             ________________________
                         N(∑(x^2)) – (∑(x))^2

# Multilinear Regression 

expression , y = b1x1 + b2x2 +.....+b0

b1,b2... - coefficient of x1,x2.... 

assuming we have n no. of observations then equation would be 

  y1 = b1X11 + b2X12+....+bkX1K
  y2=b1X21+b2X22+..+bkX2k
  
  where b1,2,.. are coefficient of hte independent variable
  
  x11, x12 ... are the independent variables for the 1st Observation
  y1,y2 -- are the dependent variable for 1st and 2nd Observations
  x21,x22 ... are the independent variables for the 2nd observations
  
  
  how to get the B1 ...bk values  
  
  we should be choosing those values such that differnet between the y's(Y(real value))  and y obtained by above equation is minimun ..
  
  b1,b2,b3 .. values should statisfy below equation 
  
       ∑M(ei) =∑(Y- (b1Xi1+b2Xi2+….+bkXik))
       
   where i can take from 1 to n 
   
   
   so , for getting these b values is key for multilinear model . this is where python comes into picture
   
   python has sklearn lib which has a linear model 
   
   from sklearn.linear_model import LinearRegression 
   
apart from this , there are two more classes which we can import for model preprocessing and post processing

from sklearn.model_selection import train_test_split - helps to split into test and train data
from sklearn.metrics import mean_squared_error - with the test data from above , can be used to evaluate the model 

one more thing , we have also have more than one dependent variable like (y11 , y12) where 

y11 = depedent variable y1 for 1st observation
y12 = depedent variable y2 for 1st observation
....
