import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump
from preprocess import prep_data

dataset = pd.read_csv("fish_participant.csv")

X, y = prep_data(dataset)

regressor = LinearRegression()
regressor.fit(X, y)

dump(regressor, "reg.joblib")

#print(X, y)