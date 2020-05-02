from sklearn.linear_model import LinearRegression
from project.data.variables import W
from project.linearRegression import mse

def regression():
    for name in W.columns.values[0:3]:
        x = W[name].to_numpy().reshape(-1, 1)
        y = W.PE.to_numpy()
        model = LinearRegression(normalize=True, fit_intercept=True).fit(x,y)
        print("{:.2f}*{}+{:.2f} = PE, R_squared = {:.3f}, MSE = ".format(
            model.coef_[0], name, model.intercept_, model.score(x,y), ))
        print(mse(model.predict(),y))
regression()