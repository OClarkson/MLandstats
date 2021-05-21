import matplotlib as plt
import numpy as np
from distributions import *






def slr(x,y):
    if type(x) == list:
        x = array(x)
    if type(y) == list:
        y = array(y)
    ybar = np.mean(y)
    xbar = np.mean(x)
    beta = np.sum((x-xbar)*(y-ybar))/np.sum((x-xbar)**2)
    alpha = ybar - beta*xbar
    liney = beta*x + alpha
    return(liney)