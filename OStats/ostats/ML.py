import numpy as np

class distributions:
    def __init__(self, disttype):
        self.subtype = disttype

def GradDes_Regression(x, y, gamma, l, epsilon = 0.0001, theta_init = None):
    '''
    theta = Coordinates of the line I'm fitting. list or array
    gamma = Step size: Currently a constant. Later I will add an adaptive method to calculate it
    X = list or array. X values of data I am fitting to.
    y list or array. Y values of the data I am fitting to.
    l = polynomial order of fit
    '''
    n = len(x)

    #create X matrix
    X_matrix = np.zeros((n,l+1))
    if theta_init is not None:
        theta = theta_init
    else:
        theta = np.zeros(l+1)
    
    for i in range(n):
        for j in range(l+1):
            X_matrix[i,j] = x[i]**j
   
    X_matrix_T = X_matrix.T #transpose of X

    #now do it
    k = 1
    kmax = 500
    J = []
    store_theta = []
    gamma_X_matrix_T = gamma*X_matrix_T
    stop_condition = False
    while not stop_condition:
        store_theta.append(theta)
        X_matrix_times_theta_miny = np.matmul(X_matrix,theta) - y
        theta = theta - np.dot(gamma_X_matrix_T,X_matrix_times_theta_miny)/n
        stop_condition = (np.abs(theta[1] - store_theta[-1][1])/store_theta[-1][1] < epsilon) and (np.abs(theta[0] - store_theta[-1][0])/store_theta[-1][0] < epsilon)
       # stop_condition = (((theta[1]-store_theta[-1][1])**2-(theta[0]-store_theta[-1][0])**2)**0.5/((store_theta[-1][1])**2-(store_theta[-1][0])**2)**0.5 < epsilon) 
        J.append(np.dot(X_matrix_times_theta_miny.T,X_matrix_times_theta_miny))
        k +=1
    print(k)
    return(store_theta, J)

