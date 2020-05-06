import numpy as np
from sklearn.linear_model import LinearRegression
from project.data.variables import W,T
from project.linearRegression import mse


def regression():
    x = np.column_stack((W.AT.to_numpy(),W.V.to_numpy(),W.AP.to_numpy()))
    y = W.PE.to_numpy()
    model = LinearRegression(normalize=True, fit_intercept=True).fit(x, y)
    print("{:.2f}*{} + {:.2f}*{} + {:.2f}*{} +{:.2f} = PE, R_squared= {:.3f}, MSE = {:.3f}".format(
        model.coef_[0], 'AT', model.coef_[1], 'V', model.coef_[2], 'AP', model.intercept_, model.score(x, y), \
            mse(model,np.column_stack((T.AT.to_numpy(),T.V.to_numpy(),T.AP.to_numpy())))))
