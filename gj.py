
import os
import sys

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from inspect import getargvalues, stack
from nested_dict import nested_dict
import time
import datetime

def printLocal(d):
    for key,val in d.items():
        print ("  - %s: %s"%(key,val))

def timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

def printFuncRun(name,loc=0):
    if loc == 0:
        print ("[%s]"%(name),timestamp())
    elif loc == 1:
        print ("[%s]"%(name),timestamp()+'\n')
    else:
        pass

def printFuncArgs():
        """Returns tuple containing dictionary of calling function's
           named arguments and a list of calling function's unnamed
           positional arguments.
        """
        #from inspect import getargvalues, stack
        posname, kwname, args = getargvalues(stack()[1][0])[-3:]
        posargs = args.pop(posname, [])
        args.update(args.pop(kwname, []))
        if len(args)>0:
            printLocal(args)
        if len(posargs)>0:
            print (posargs)
        return args, posargs
    
def ls_ls_common(ls_ls,return_ls=1):
    if return_ls:
        return list(set(ls_ls[0]).intersection(*ls_ls))

def ls_ls_union(ls_ls,return_ls=1):
    if return_ls:
	    return list(set(ls_ls[0]).union(*ls_ls))
    
    
# matrix correlation plot
def df_corr_matrix_plot(df,savefn=None,size=4,rot=30,share_x_y=1,hue=None,diag='kde'):
    print df.info
    print df.describe() 
    #g = sns.PairGrid(df.fillna(0,inplace=1), palette=["red"],size=size)
    g = sns.PairGrid(df, palette=["red"],size=size,hue=hue)
    g.map_lower(plt.scatter, s=10)
    g.map_upper(corrfunc,coor='pearson')
    #g.map_diag(sns.distplot, hist=False, rug=True)
    if diag == 'kde':
        g.map_diag(sns.kdeplot)
    if diag == 'violin':
        g.map_diag(sns.violinplot)
    if diag == 'hist':
        g.map_diag(plt.hist)
    
    x_min_ls,x_max_ls,y_min_ls,y_max_ls = [],[],[],[]
    for ax in g.axes.flat:  
        plt.setp(ax.get_xticklabels(), rotation=rot)
        x_min_ls.append(ax.get_xlim()[0])
        x_max_ls.append(ax.get_xlim()[1])
        y_min_ls.append(ax.get_ylim()[0])
        y_max_ls.append(ax.get_ylim()[1])
    if share_x_y > 0:
       
        axis_min=min(min(x_min_ls),min(y_min_ls))
        axis_max=max(max(x_max_ls),max(y_max_ls))
        df_min=df.min().min()
        df_max=df.max().max() # df.values.max()
        df_min=df.describe().loc['min',:].min()
        df_max=df.describe().loc['max',:].max()
        for ax in g.axes.flat:
            ax.set_xlim(df_min,df_max)
            ax.set_ylim(df_min,df_max)
            #ax.set_xlim(axis_min,axis_max)
            #ax.set_ylim(axis_min,axis_max)
            #ax.set_xlim(min(x_min_ls),max(x_max_ls))
            #ax.set_ylim(min(y_min_ls),max(y_max_ls))

    """
    for i in xrange(df.shape[0]):
        label=g.axes[-1,i].get_xlabel()
        g.axes[-1,i].set_xlabel("") # set xlable invisiable
        g.axes[i,0].set_ylabel("")
        ax=g.axes[i,i]
        ax.set_title(label)
        ax.annotate("%s"%(label),
                    xy=(.5, .9),ha='center',va='center',fontsize=20, xycoords=ax.transAxes)
    """

    if savefn:
        g.savefig(savefn)
    plt.close()
    
    
    
