import numpy as np

class distributions:
    def __init__(self, disttype):
        self.subtype = disttype

#class regression:
#    def __init__(self, subtype):
#    self.subtype = subtype
    
    
def GradDes_Regression(x, y, gamma, epsilon = 0.0001, theta_init = None, n = 1):
    '''
    gamma = Step size: Currently a constant. Later I will add an adaptive method to calculate it
    X = list or array. X values of data I am fitting to.
    y = list or array. Y values of the data I am fitting to.
    n = number of variables 
    theta_init = initial guesses for theta...list/vector
    '''
    m = len(y) #number of points
    ones_list = np.ones(m)
    X_matrix = np.vstack((ones_list,x)).T
    X_matrix_T = X_matrix.T #transpose of X

    if theta_init is not None:  
        theta = theta_init
    else:
        theta = np.zeros(n+1)

    #now do it
    k = 1
    J = []
    store_theta = []
    gamma_X_matrix_T = gamma*X_matrix_T
    stop_condition = False
    while not stop_condition:
        store_theta.append(theta)
        X_matrix_times_theta_miny = np.matmul(X_matrix,theta) - y
        theta = theta - np.dot(gamma_X_matrix_T,X_matrix_times_theta_miny)/m
        stop_condition = (np.abs(theta[1] - store_theta[-1][1])/store_theta[-1][1] < epsilon) and (np.abs(theta[0] -\
        store_theta[-1][0])/store_theta[-1][0] < epsilon)
       # stop_condition = (((theta[1]-store_theta[-1][1])**2-(theta[0]-store_theta[-1][0])**2)**0.5/((store_theta[-1]\
       # [1])**2-(store_theta[-1][0])**2)**0.5 < epsilon) 
        J.append(np.dot(X_matrix_times_theta_miny.T,X_matrix_times_theta_miny))
        k +=1
    
    
   #create h matrix
#    print(len(X_matrix[0]),len(X_matrix))
#    h_theta = np.zeros(len(X_matrix[0])) 

        
    return(store_theta, J)




def Normal_Linear_Regression(x, y):
    m = len(y) #number of points
    assert m <1e4

    ones_list = np.ones(m)
    X_matrix = np.vstack((ones_list,x)).T   
    #print(X_matrix)
    XTX = np.dot(X_matrix.T,X_matrix)
    XTy = np.dot(X_matrix.T,y)
    xpinv = np.linalg.inv(XTX)
    theta = np.dot(xpinv,XTy) 

    return(theta)


def simplelinearregression(x,y):
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

def thetato_y(x,y,theta):
    m = len(y)
    ones_list = np.ones(m)
    X_matrix = np.vstack((ones_list,x)).T
    #print(theta)
    h = np.matmul(X_matrix,theta.T)
            
    return(h)
