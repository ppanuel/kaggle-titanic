# -*- coding:utf-8 -*-

import pandas as pd
from titanicFunc import cleanData, dropUselessStuff
from sklearn.ensemble import RandomForestClassifier


# Loading the data
datasDirectory = 'S:\\Projets\\AI\\kaggle\\titanic\\datas\\'
train = pd.read_csv(datasDirectory + 'train.csv')
test  = pd.read_csv(datasDirectory + 'test.csv')

# Clean the data
_train = cleanData(train)
_test  = cleanData(test)
cleanedTrain = dropUselessStuff(_train)
cleanedTest  = dropUselessStuff(_test)

# Train the data
X_train = cleanedTrain.drop('Survived', axis=1)
y_train = cleanedTrain['Survived']

print('Random Forest')
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print('Score: ', model.score(X_train, y_train))

# Prediction on test set
X_test = cleanedTest.drop('PassengerId', axis=1).copy()
y_test = model.predict(X_test)

# Submission
submit = pd.DataFrame({'PassengerId': cleanedTest['PassengerId'], 'Survived': y_test})
submit.to_csv(datasDirectory+'submit1.csv', index=False)