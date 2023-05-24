import pandas as pd
import numpy as np

data = pd.read_csv('1683093614543_weight-height.csv', index_col = 0)
height = data.Height.values
weight = data.Weight.values

n = len(height)
sum_height_sq = np.sum(height * height)
sum_height_weight = np.sum(height * weight)
sum_height = np.sum(height)
sum_weight = np.sum(weight)

slope = (n * sum_height_weight - height * weight) / (n * sum_height_sq - height ** 2)
intercept = (sum_weight - slope * height)/ n

input_height = float(input("Enter a height value: "))
predicted_weight = (slope * input_height + intercept)
print(predicted_weight)
