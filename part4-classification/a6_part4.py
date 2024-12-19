import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male', 'Female'], [0, 1], inplace=True)

# Feature selection (X) and target (y)
x = data[["Age", "EstimatedSalary", "Gender"]]
y = data["Purchased"]

# Step 1: Print the values for x and y
print("X values (features):")
print(x)
print("Y values (target):")
print(y)

# Step 2: Standardize the data using StandardScaler
scaler = StandardScaler().fit(x)  
x_scaled = scaler.transform(x) 

# Step 3: Transform the data (done in the previous step)

# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Step 5: Fit the model with logistic regression
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)

# Step 6: Print the score to see the accuracy of the model
print("Accuracy:", model.score(x_test, y_test))

print("*************")
print("Testing Results:")
print("")

# Step 7: Print out the actual y_test values and predicted y values
for index in range(len(x_test)):
    x_single = x_test[index].reshape(1, -1)  
    y_pred = int(model.predict(x_single))

    if y_pred == 0:
        y_pred_label = "Not Purchased"
    elif y_pred == 1:
        y_pred_label = "Purchased"
    
    actual = y_test.iloc[index] 
    if actual == 0:
        actual_label = "Not Purchased"
    elif actual == 1:
        actual_label = "Purchased"
    
    print(f"Predicted: {y_pred_label} | Actual: {actual_label}")
    print("")

# Prediction for a new individual
individual = pd.DataFrame({
    "Age": [34],
    "EstimatedSalary": [56000],
    "Gender": [1] 
})

individual_scaled = scaler.transform(individual[["Age", "EstimatedSalary", "Gender"]])

prediction = model.predict(individual_scaled)

if prediction == 0:
    prediction_label = "Not Purchased"
else:
    prediction_label = "Purchased"

print(f"Prediction for 34-year-old female earning $56,000: {prediction_label}")