import numpy as np
import pandas as pd

def calculate_prob(x, mean, variance):
    exponent = np.exp(-(x - mean)**2 / (2 * variance))
    return exponent / np.sqrt(2 * np.pi * variance)

data = pd.read_csv('1683093619109_Iris.csv', index_col=0)
data['Species'].replace('Iris-setosa',1,inplace=True)
data['Species'].replace('Iris-versicolor',2,inplace=True)
data['Species'].replace('Iris-virginica',3,inplace=True)

class_label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

AM = np.zeros((len(features), len(class_label)))
AV = np.zeros((len(features), len(class_label)))

for i, label in enumerate(class_label, start=1):
    clas = data[data['Species'] == i]
    for j, feature in enumerate(features):
        AM[j, i-1] = np.mean(clas[feature])
        AV[j, i-1] = np.var(clas[feature])

print("Enter inputs:")
x = [float(input(f"Enter the {feature}: ")) for feature in features]

A = np.array([calculate_prob(x[i], AM[i], AV[i]) for i in range(len(features))])

print(A)

predicted_class = class_label[np.argmax(np.prod(A, axis=0))]
print(predicted_class)
