
import pandas as ps


url = 'http://bit.ly/w-data'
my_data = ps.read_csv(url)

my_data.head(10)
print("Read data successfully. Number of records read : ",len(my_data))
print('Printing first 10 records')
print(my_data.head(10))

X = my_data.iloc[:, :-1].values  
y = my_data.iloc[:, 1].values 

#splitting the data into training and test sets

from sklearn.model_selection import train_test_split
print('-------------------------------------')
print()

print("**** Splitting the samples into train and test sets ****")
print()
#test_size tells the proportion of the dataset to include in the test split
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

print('Number of Samples of X, y',len(X))
print('Number of train samples of X',len(X_train))
print('Number of test samples of X',len(X_test))

#Now let's use the train samples to get a regression model
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

print('------------------------------------')
print("******.  Model training complete  *******")
print()
#Now using this model let's predict the scores for the test samples of hours
# linear regression model is a line of the form y=mX + c, m - slope, c- intercept

r_sq = regressor.score(X_train,y_train)

print('Coefficient of determination: ', r_sq)
print('intercept (b0) : ',regressor.intercept_)
print('slope (b1) : ', regressor.coef_)

line = regressor.coef_ * X + regressor.intercept_

print('-------------------------------------')
print()
#using this model we can predict
y_pred = regressor.predict(X_test)

df = ps.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df)

#Let's evaluate the model
from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred)) 

#We can predict any value

hours = [[9.25],]
y_pred = regressor.predict(hours)

print('---------------------------------------')
print("Number of hours studied",hours)
print("Predicted Scored :",y_pred)

print("Plotting the original samples as scatter plot and regressor as line")
import matplotlib.pyplot as plt

plt.scatter(X,y,color='red')
plt.plot(X,line,color='blue')
plt.show()
