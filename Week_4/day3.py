from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

X = [[2], [6], [4], [1], [3]]

y = ["Fail", "Pass", "Pass", "Fail", "Pass"]

model.fit(X, y)

prediction = model.predict([[0]])

print(prediction)