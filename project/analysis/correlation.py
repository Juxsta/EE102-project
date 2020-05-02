#%% Imports
from project.data.variables import W

#%%
def getCorrelation():
#%% Correlation Coefficient
    df = W.corr(method="pearson")
    for name,index in zip(df.columns.values[0:4],range(0,4)):
        print(f"For {name}: r = {df.iloc[4,index]}")
    print('As expected RH has the lowest correlation coefficient')
# %%
