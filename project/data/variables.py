#%% Initializing Testing and Working Data
from pandas import read_excel, DataFrame
import os 
dirpath = os.getcwd()
join = lambda path: os.path.join(dirpath,path)
L = read_excel(f'{os.path.dirname(os.path.realpath(__file__))}/PPDataSheet.xlsx')
W:DataFrame = L[:7769] # working set
T:DataFrame = L[7700:] # testing 
W.to_csv(join('Working Set.csv'))
T.to_csv(join('Testing Set.csv'))
# %%
