import base as b 
import matplotlib.pyplot as plt 
import events as ev
from plotting import plot_distribution

def plot_distributions_seasons(
        df, 
        quiet_level = 4
        ):
    

    fig, ax = plt.subplots(
        ncols = 2,
        nrows = 2, 
        figsize = (15, 8), 
        sharex = True, 
        sharey = True, 
        dpi = 300
        )
    
    ks = {
         
         3:  'march equinox',
         6:  'june solstice',
         9:  'setember equinox',
         12: 'december solstice'
         }
    
    plt.subplots_adjust(wspace = 0.1)
    
    for i, ax in enumerate(ax.flat):
        
        month = (i + 1) * 3
        season_name = ks[month]
        
        count = []
        name = [f'$Kp \\leq$ {quiet_level}', 
                f'$Kp >$ {quiet_level}']
        
        for i, level in enumerate(ev.kp_levels(
                df, quiet_level = quiet_level)
                ):
            index = i + 1
            ds = ev.seasons(level, month)
        
            c = plot_distribution(
                    ax, 
                    ds, 
                    f'({index}) {name[i]}'
                    )
            
            count.append(f'({index}) {c} events')
        
        infos = ('EPB occurrence\n' + 
                 '\n'.join(count))
            
        ax.text(
                0.65, 0.25, 
                infos, 
                transform = ax.transAxes
                )
        
        ax.set(title = season_name.title(),
               ylim = [-0.2, 1.2])
    
    
    ax.legend(ncol = 2, 
              bbox_to_anchor = (-.1, 2.6),
              loc = "upper center")
    
    fontsize = 25
    fig.text(
        0.05, 0.25, 
        "EPB occurrence probability", 
        fontsize = fontsize, 
        rotation = 'vertical'
        )
    
    fig.text(
        0.4, 0.05, 
        "$\\gamma_{FT}~$ ($\\times 10^{-3}~s^{-1}$)", 
        fontsize = fontsize)
    
def main():
    df = b.load('all_results.txt')
    
    df = df.loc[~(df['all'] > 3.5)]
    
    df['doy'] = df.index.day_of_year.copy()
    
    plot_distributions_seasons(df)
    
main()