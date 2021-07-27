import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

my_data = np.genfromtxt('Student_Scores.csv',delimiter=',',names='Hours,Scores')

#get the hours data as input array
x=my_data['Hours']
y=my_data['Scores']
my_data.reshape(-1,1)
print('Hours','Scores')
print(x,y)

#for h,s in my_data.reshape(-1,1) :
#	print(h,s)
#	

model = LinearRegression()

x=x.reshape(-1,1)
model.fit(x,y)

r_sq = model.score(x,y)

print('Coefficient of determination: ', r_sq)

print('intercept (b0) : ',model.intercept_)

print('slope (b1) : ',model.coef_)

y_new = model.predict(x)

print('y_new : ',y_new)

plt.scatter(x,y,color='red')
plt.plot(x,y_new,color='blue')
plt.show()

#predicted score for hours of study = 9.25 hours/day
hours_of_study = 9.25
predicted_score = model.predict(hours_of_study)
                      
print("Hours of Study : ", "Predicted Score")
print("------------------------------------")
print(hours_of_study)



