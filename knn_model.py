import pandas as pd
from sklearn.model_selection import train_test_split as t_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier as kn_classifier
from sklearn.utils import shuffle

data = pd.read_csv("D:\\University Documents\\Assignments\\6th Semester\\Artificial Intelligence\\Lab1\\iris.csv")
print(data.head())

data = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'variety']]
X = data.iloc[:, :-1]
Y = data.iloc[:, 4]

X_train, X_test, Y_train, Y_test = t_split(X, Y, test_size=0.20)
classifier = kn_classifier(n_neighbors=9)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(f"Accuracy is: {accuracy_score(Y_pred, Y_test)}")
