import numpy as np
from sklearn.linear_model import LinearRegression
from project.data.variables import W,T
from project.linearRegression import mse


def regression():
    getX = lambda set,name: set[name].to_numpy().reshape(-1,1)
    for name1 in W.columns.values[:2]:
        for name2 in W.columns.values[1:3]:
            if(name1 == name2): continue
            x = np.column_stack((W[name1].to_numpy(), W[name2].to_numpy()))
            testX = np.column_stack((T[name1].to_numpy(), T[name2].to_numpy()))
            y = W.PE.to_numpy()
            model = LinearRegression(normalize=True, fit_intercept=True).fit(x,y)
            print("{:.2f}*{} + {:.2f}*{} + {:.2f} = PE, R_squared= {:.3f}, MSE = {:.3f}".format(
                model.coef_[0], name1, model.coef_[1], name2, model.intercept_, model.score(x,y),mse(model,testX) ))
