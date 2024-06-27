# lib manipulation data
import pandas as pd
import numpy as np

# lib praproses data
from sklearn.preprocessing import MinMaxScaler

# func getData by csv file
def getDataset(df):

  # load dataset
  dataset = pd.read_csv("../../dataset/"+df)
  return dataset

# func normalized by min-max method
def normalized(df):

  # Set features and Labels
  x = df[["sepal_length","sepal_width","petal_length","petal_width"]].values
  y = df["species"].values

  # prosess normalized data
  scaler = MinMaxScaler(feature_range=(-1, 1))
  scaled = scaler.fit_transform(x)

  # convert numpy to pandas dataframe
  results = pd.concat([
    pd.DataFrame(scaled, columns=["sepal_length","sepal_width","petal_length","petal_width"]),
    pd.DataFrame(y, columns=["species"]),
  ], axis=1)

  # return values
  return results