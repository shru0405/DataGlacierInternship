import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv(r"C:\Users\shrut\PycharmProjects\FlaskDeploy\hiring.csv")

x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))