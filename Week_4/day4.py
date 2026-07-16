from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

model = DecisionTreeClassifier()

X = [[8], [6], [4], [1], [5]]

y = ["Pass", "Pass", "Fail", "Fail", "Pass"]

X_train, X_test , y_train , y_test = train_test_split(X, y, test_size= 0.2, random_state = 15)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction)

print(X_test)
print(y_test)

accuracy = accuracy_score(y_test, prediction)

print(accuracy)