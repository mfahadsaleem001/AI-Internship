from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

X = [[8], [6], [4], [1], [5]]

y = ["Pass", "Pass", "Fail", "Fail", "Pass"]

model.fit(X, y)

prediction = model.predict([[2]])

print(prediction)