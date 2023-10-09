import pandas as pd

dataFile = pd.read_csv("data/ad_data.csv")

ages = dataFile['age'].values

gender = dataFile['gender'].values

store = dataFile['store'].values

relevant = dataFile['relevant'].values

print(dataFile)