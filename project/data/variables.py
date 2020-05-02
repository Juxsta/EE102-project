#%% Initializing Testing and Working Data
from pandas import read_excel, DataFrame
import os 
L = read_excel(f'{os.path.dirname(os.path.realpath(__file__))}/PPDataSheet.xlsx')
W:DataFrame = L[:7769] # testing set
T:DataFrame = L[7700:] # working setread_excel()
# %%
