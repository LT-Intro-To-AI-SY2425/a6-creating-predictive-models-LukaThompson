# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
Without the standard scaler, the accuracy is 0.65. The model is a lot less accurate when there is no standard scale because the data is not being standardized which lowers the quality of the data
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
When there is a standard scalar, the accuracy is 0.8875 which is accurate enough for the given case because it is predicting weather someone has a certain type of car or not which 88.75% accuracy is good for
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
When there was no StandardScalar, the model only predicted no even when it sould have predicted yes so that was a pattern in the model but I couldn't find a concrete pattern of incorrect guesses. The model was very accurate when using the StandardScalar and when it was wrong, it did not have much of a pattern.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
The model predicts that they would not have an SUV
