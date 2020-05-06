from project.data.variables import L,T,W
from project.analysis import scatterPlot,correlation
from project.linearRegression import oneVariable,twoVariable,threeVariable

def run():
    print(W.describe())
    scatterPlot.scatterPlot()
    print("Obtaining Correlation Coefficients:")
    correlation.getCorrelation()
    print('Performing one variable regression:')
    oneVariable.regression()
    print('Performing two variable regression:')
    twoVariable.regression()
    print('Performing three variable regression:')
    threeVariable.regression()
# %%
