from project.data.variables import L,T,W
from project.analysis import scatterPlot,correlation
from project.linearRegression import oneVariable,twoVariable,threeVariable

def run():
    print("Working Data")
    print(W.describe())
    print("Median\n",W.median())
    print(f"Mode\n {W.mode()}")
    print(f"Variance\n {W.var()}")
    
    print("Test Data")
    print(T.describe())
    print("Median\n",T.median())
    print(f"Mode\n {T.mode()}")
    print(f"Variance\n {T.var()}")
  
    print("Testing Data")
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
