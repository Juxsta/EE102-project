import numpy as np
from sklearn.linear_model.base import LinearRegression
from project.data.variables import T,L
from project.linearRegression.normalize import normalize
T=normalize(T)
def mse(model:LinearRegression,X):
    m=(len(L)-7700)
    return np.sum((T["PE"]-model.predict(X))**2/m)