from sklearn.linear_model import LinearRegression
from project.data.variables import W,T
from project.linearRegression import mse,normalize
import matplotlib.pyplot as plt
import os
dirpath = os.getcwd()
W=normalize(W)
T=normalize(T)
def regression():
    for name in W.columns.values[0:3]:
        x = W[name].to_numpy().reshape(-1, 1)
        y = W.PE.to_numpy()
        model = LinearRegression(fit_intercept=True).fit(x,y)
        
        print("{:.2f}*{}+{:.2f} = PE, R_squared = {:.3f}, MSE = {:.3f}".format(
            model.coef_[0], name, model.intercept_, model.score(x,y), \
                mse(model,T[name].to_numpy().reshape(-1,1))))
        plt.scatter(W[name],W['PE'])
        # plt.scatter(model.coef_*x+model.intercept_,W['PE'],marker=0)
        plt.plot(x,model.predict(x),'r--')
        plt.suptitle(f"{name} vs PE")
        plt.text(0.6,0.8,'R-squared = {:.3f}'.format(model.score(x,y)))
        plt.savefig(f"{dirpath}/One Variable {name} vs PE.png")
        plt.clf()
