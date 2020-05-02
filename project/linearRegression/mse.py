import numpy as np
from sklearn.linear_model.base import LinearRegression
def mse(model:LinearRegression,x:np.ndarray,y:np.ndarray):
    model.predict()