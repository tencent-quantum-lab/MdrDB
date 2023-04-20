import os
import pandas as pd
import numpy as np
import warnings
import random
warnings.filterwarnings('ignore')

import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

import pickle
import json

# ======================================
# Function we will use for scatter plots
# ======================================
def plot_corr(ax, x, y, xerr=None, yerr=None, xlim=[-5,+5], ylim=[-5,+5], title='', legendloc=None,
              fit=True, diagonal=True, labelsize=16, msize=90, yax=1.36, xax=1.36,
              colorbar=False, vmin=0.0, vmax=2.8, cbarlabel='cbar', cbar_shrink=1.0, cbar_pad=0.15):
  
    # the absolute error for each data point
    diff = np.abs(x-y)
    cmap = plt.cm.coolwarm
    
    SC = ax.scatter(x=x, y=y, c=diff, cmap=cmap, s=msize, edgecolors='k', linewidths=1.2, zorder=10, 
                vmin=0.0, vmax=2.8, label='_nolegend_')
    
    if yerr is None and xerr is not None:
        ax.errorbar(x=x, y=y, xerr=xerr, fmt=None, marker=None, 
                color='k', linewidth=1.2, zorder=0, label='_nolegend_')
    elif yerr is not None and xerr is not None:
        ax.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, fmt='none', marker=None, 
                color='k', linewidth=1.2, zorder=0, label='_nolegend_')
    
    # Make ColorBar
    if colorbar is True:
        cbarticks = [0.0, 0.7, 1.4, 2.1, 2.8]
        cbar = fig.colorbar(SC, ax=ax, shrink=cbar_shrink, pad=cbar_pad, ticks=cbarticks)
        cbar.set_label(cbarlabel, fontsize=labelsize)
        cax = plt.gcf().axes[-1]
        cax.tick_params(labelsize=labelsize)
    
    # Ticks and labels
    ax.set_xlabel(r'Experimental $\Delta\Delta G$, kcal/mol', fontsize=labelsize)
    ax.set_ylabel(r'Calculated $\Delta\Delta G$, kcal/mol', fontsize=labelsize)
  
    ax.tick_params(axis='x', labelsize=labelsize)
    ax.tick_params(axis='y', labelsize=labelsize)
    
    xmin = min(xlim)
    xmax = max(xlim)
    ymin = min(ylim)
    ymax = max(ylim)
    
    if title != '':
        ax.set_title(title, fontsize=labelsize*1.2)
    
    # add diagonal
    if diagonal is True:
        ax.plot([xmin,xmax], [xmin,xmax], '--', color='gray')

    # add zero axes
    ax.axvline(x=xax, color='k', linestyle='-', linewidth=1.2)
    ax.axhline(y=yax, color='k', linestyle='-', linewidth=1.2)
    
    # shaded area indicating 1,2 kcal/mol errors
    a = [xmin,xmax]
    b = [j+1.4 for j in a]
    c = [j-1.4 for j in a]
    ax.fill_between(a, b, c, alpha=0.1, interpolate=True, color='k')
    
    # Linear fit
    if fit is True:
        fit = np.polyfit(x, y, 1)
        fit_fn = np.poly1d(fit)
        x_fit = np.linspace(xmin, xmax, len(x)) 
        y_fit = fit_fn(x_fit)
        ax.plot(x_fit, y_fit, '-', color='k', zorder=1, 
                label='$\Delta\Delta G_{calc} = %.2f \cdot \Delta\Delta G_{exp} %+.2f$' %(fit[0],fit[1]))

    # grid
    ax.grid(b=True, which='major', color='0.5',linestyle=':')

    ax.set_xlim([xmax,xmin])
    ax.set_ylim([ymax,ymin])
    
    # Make box square
    x0,x1 = ax.get_xlim()
    y0,y1 = ax.get_ylim()
    ax.set_aspect(aspect=(x1-x0)/(y1-y0))
    
    # make legend
    if legendloc is not None:
        legend = ax.legend(loc=legendloc, prop={'size':labelsize*0.8})