# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:05:34 2023

@author: Luiz
"""

import numpy as np
import matplotlib.pyplot as plt
import base as b
import events as ev 
from plotting import plot_distribution



b.config_labels()



def plot_distributions_solar_flux(
        df, 
        col = 'gamma',
        level = 100
        ):
    
    
    fig, ax = plt.subplots(
        dpi = 300, 
        sharex = True,
        sharey = True,
        figsize = (12, 6)
        )
        
    labels = [
        '$F_{10.7} < $' + f' {level}',
        '$F_{10.7} > $' + f' {level}'
        ]
    
    if col == 'gamma':
        vmin, vmax, step = 0, 4, 0.2
        
    elif col == 'vp':
        vmin, vmax, step = 0, 85, 5
    else:
        vmin, vmax, step = 0, 1, 0.05
    
    solar_dfs =  ev.solar_levels(
        df, 
        level,
        flux_col = 'f107a'
        )
     
    total = []
    
    for i, ds in enumerate(solar_dfs):
    
        c = plot_distribution(
            ax, 
            ds,
            limits = (vmin, vmax, step),
            col = col,
            label = f'{labels[i]}'
            )
        
        total.append(c)
    
    if col == 'vp':
        xlabel = b.y_label('vp')
        vmax = 70
    else:
        xlabel = b.y_label('gamma')
        
        
    ax.set(
        xlim = [vmin, vmax],
        xticks = np.arange(vmin, vmax + step, step * 2),
        ylim = [-0.2, 1.3],
        yticks = np.arange(0, 1.25, 0.25),
        )
        
    ax.legend(ncol = 2, loc = 'upper center')
    
    info = f' ({sum(total)} EPBs events)'
    
    ax.set(
        title = df.columns.name + info,
        xlabel = xlabel, 
        ylabel = 'EPB occurrence probability'
        )
    
    return fig
 

df = ev.concat_results('saa')

col = 'vp'


fig = plot_distributions_solar_flux(
    df, 
    col, 
    level = 86
    )

FigureName = f'PD_{col}_effects'

fig.savefig(b.LATEX(FigureName), dpi = 400)

# dfs =  ev.solar_levels(
#     df, 
#     level =  86,
#     flux_col = 'f107a'
#     )

