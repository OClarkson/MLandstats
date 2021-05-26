import matplotlib.pyplot as plt
import numpy as np


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
           
                   

def ColorGradient(start = (256,256,256), stop=(0,0,0), n=2):
    '''
    Pick two colour and gives back gradient of those colours
    '''
    gradR = np.linspace(start[0]/256,stop[0]/256,n)
    gradG = np.linspace(start[1]/256,stop[1]/256,n)
    gradB = np.linspace(start[2]/256,stop[2]/256,n)
    gradient = []
    for i in range(n):
        gradient.append((gradR[i],gradG[i],gradB[i]))


    return gradient