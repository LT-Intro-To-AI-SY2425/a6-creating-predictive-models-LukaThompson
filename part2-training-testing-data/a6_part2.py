import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values


random_seed = 42  

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=random_seed)

xtrain = xtrain.reshape(-1,1)
xtest = xtest.reshape(-1, 1)

model = LinearRegression().fit(xtrain, ytrain)
coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)
print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", r_squared)
'''
**********TEST THE MODEL**********
'''
predict = model.predict(xtest)
predict = np.around(predict, 2)
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print("x value:", float(x_coord[0]), "Predicted y value:", predicted_y, "Actual y value:", actual)
print("\nTesting Linear Model with Testing Data:")


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(5,4))

plt.scatter(xtrain,ytrain, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")

plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")
x_range = np.linspace(min(x), max(x), 100).reshape(-1, 1)
plt.plot(x_range, model.predict(x_range), c="r", label="Line of Best Fit")

plt.legend()
plt.show()