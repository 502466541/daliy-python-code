
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
        
        
        
