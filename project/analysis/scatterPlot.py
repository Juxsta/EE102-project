#%% Creating scatterplots
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from project.data.variables import W
#%%
def scatterPlot():
#%% Plotting
    for name in W.columns.values[0:4]:
        plt.scatter(W[name], W['PE'])
        plt.xlabel(name)
        plt.ylabel('PE')
        plt.title(f'{name} vs PE')
        plt.show()
    print("From the plots Ambient Temperature has the greatest effect on PE\n\
        RH has a low correlation coefficient")
# RH does not influence PE very much")
