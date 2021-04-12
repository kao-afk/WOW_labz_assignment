import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd

d=pd.read_csv("trainingdata.txt",sep="\t")
X=d["Sleep hours"].values
y=d["Active hours"].values

X=X.reshape(-1,1)
reg = LinearRegression().fit(X, y)

## saving the model
file_name = "model.pkl"
pickle.dump(reg, open(file_name, "wb"))