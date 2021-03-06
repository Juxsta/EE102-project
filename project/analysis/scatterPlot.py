#%% Creating scatterplots
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from pandas import DataFrame
from project.data.variables import W
import itertools
import numpy as np
import matplotlib.pyplot as plt
import os
dirpath = os.getcwd()
output_path = os.path.join(dirpath,'scatterplot.png')
#%%
def scatterplot_matrix(df:DataFrame, names, **kwargs):
    """Plots a scatterplot matrix of subplots.  Each row of "data" is plotted
    against other rows, resulting in a nrows by nrows grid of subplots with the
    diagonal subplots labeled with "names".  Additional keyword arguments are
    passed on to matplotlib's "plot" command. Returns the matplotlib figure
    object containg the subplot grid."""
    data = np.empty((len(df.columns.values),len(df.index)))
    for name,index in zip(df.columns.values,range(0,len(df.columns.values))):
        data[index] = df[name]
    numvars, numdata = data.shape
    fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(8,8))
    fig.subplots_adjust(hspace=0.05, wspace=0.05)

    for ax in axes.flat:
        # Hide all ticks and labels
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        # Set up ticks only on one side for the "edge" subplots...
        if ax.is_first_col():
            ax.yaxis.set_ticks_position('left')
        if ax.is_last_col():
            ax.yaxis.set_ticks_position('right')
        if ax.is_first_row():
            ax.xaxis.set_ticks_position('top')  
        if ax.is_last_row():
            ax.xaxis.set_ticks_position('bottom')

    # Plot the data.
    for i, j in zip(*np.triu_indices_from(axes, k=1)):
        for x, y in [(i,j), (j,i)]:
            axes[x,y].plot(data[x], data[y], **kwargs)

    # Label the diagonal subplots...
    for i, label in enumerate(names):
        axes[i,i].annotate(label, (0.5, 0.5), xycoords='axes fraction',
                ha='center', va='center')

    # Turn on the proper x or y axes ticks.
    for i, j in zip(range(numvars), itertools.cycle((-1, 0))):
        axes[j,i].xaxis.set_visible(True)
        axes[i,j].yaxis.set_visible(True)

    return fig
def scatterPlot():
    columns = W.columns.tolist()
    columns = columns[::-1]
    df = W[columns]
    fig = scatterplot_matrix(df, df.columns.values,
            linestyle='none', marker='.', color='blue', mfc='none')
    fig.suptitle('ScatterPlot Matrix')
    plt.savefig(output_path)
    #%%

# %%
