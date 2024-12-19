# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The r squared coefficient for my model is 0.86. This means that the model is close to the data 
2. Is your model accurate? Why or why not?
The model is accurate because the R squared value is 0.86 which means that the model is 86% accurate when guessing
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
It predicts that a car that is 10 years old with 89000 miles is worth 9205.45 dollars and a car that is 20 years old with 150000 miles is worth 2051.56
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
The model is trained as a slope which means that eventually, the price will become negative. This happens because the data has not been trained on cars that are very old so it predics the price based on what it knows which makes the value negative. This will happen because a best fit line is used so it cant show exponential growth this means that at some point, the bfl will go negative