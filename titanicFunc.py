# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

def cleanData(data):
	data['Fare'] = data['Fare'].fillna(data['Fare'].median())
	data['Price'] = 1
	data.loc[data.Fare >= data.Fare.mean(), 'Price'] = 0
	data.Price.astype(int)

	data['Age']  = data['Age'].fillna(data['Age'].median()).astype(int)		# Possible amelioration: adjust median according to Pclass
	data['Young'] = 0
	data.loc[data.Age <= 18, 'Young'] = 1
	data['Adult'] = 0
	data.loc[(data.Age.any() > 18) & (data.Age.any() <= 50), 'Adult'] = 1
	data['Old'] = 0
	data.loc[data.Age > 50, 'Old'] = 1
	data.Young.astype(int)
	data.Adult.astype(int)
	data.Old.astype(int)

	data['Sex'] = data['Sex'].map({'male':0, 'female':1}).astype(int)

	data['Embarked'] = data['Embarked'].fillna('S')
	data['Embarked'] = data['Embarked'].map({'S':0, 'C':1, 'Q':1}).astype(int)

	data['Title'] = data['Name'].str.extract('([\w]+)\.', expand=False)
	#data['Title'] = data['Title'].replace(['Dr', 'Rev', 'Major', 'Col', 'Don','Countess', 'Lady', 'Capt', 'Sir','Jonkheer'], 'Rare')
	data['Title'] = data['Title'].replace(['Dr', 'Rev', 'Major', 'Col', 'Don', 'Capt', 'Sir', 'Jonkheer'], 'Mr')
	data['Title'] = data['Title'].replace(['Mlle', 'Ms'], 'Miss')
	data['Title'] = data['Title'].replace(['Dona', 'Countess', 'Lady', 'Mme'], 'Mrs')
	data['Title'] = data['Title'].map({'Mr':0, 'Mrs':1, 'Miss':2, 'Master':3}).astype(int)
	data['Mr'] = 0
	data['Mrs'] = 0
	data['Miss'] = 0
	data['Master'] = 0
	data.loc[data.Title == 0, 'Mr'] = 1
	data.loc[data.Title == 1, 'Mrs'] = 1
	data.loc[data.Title == 2, 'Miss'] = 1
	data.loc[data.Title == 3, 'Master'] = 1
	data.Mr.astype(int)
	data.Mrs.astype(int)
	data.Miss.astype(int)
	data.Master.astype(int)


	data['Alone'] = 0
	data.loc[data['SibSp'] + data['Parch'] == 0, 'Alone'] = 1


	#data['AgeAndClass'] = data.Age * data.Pclass

	return data


def dropUselessStuff(data):
	data = data.drop(['Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Fare', 'Age', 'Title'], axis=1)

	if 'Survived' in data:
		data = data.drop(['PassengerId'], axis=1)

	return data