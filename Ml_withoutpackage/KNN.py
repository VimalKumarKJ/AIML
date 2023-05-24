import pandas as pd
import numpy as np

data = pd.read_csv("1683093619109_Iris.csv", index_col=0)
data['Species'].replace('Iris-setosa',1,inplace = True)
data['Species'].replace('Iris-vercicolor',2,inplace = True)
data['Species'].replace('Iris-virginica',3,inplace = True)
class_label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

print("Enter the input:")
sample = [float(input(f"Enter the {feature}: ")) for feature in features]
k = 75
data['Distance'] = np.sum((data[features] - sample) ** 2, axis=1)
sorted_data = data.sort_values(by='Distance')
output = sorted_data.iloc[:k, 4]
predicted_class = class_label[output.values[0] - 1]

print(predicted_class)