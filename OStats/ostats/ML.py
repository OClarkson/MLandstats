import numpy as np

class distributions:
    def __init__(self, disttype):
        self.subtype = disttype

class regression:
    def __init__(self, subtype):
    self.subtype = subtype
    
    
    def GradDes_Regression(x, y, gamma, l, epsilon = 0.0001, theta_init = None):
        '''
        theta = Coordinates of the line I'm fitting. list or array
        gamma = Step size: Currently a constant. Later I will add an adaptive method to calculate it
        X = list or array. X values of data I am fitting to.
        y list or array. Y values of the data I am fitting to.
        l = polynomial order of fit
        '''
        m = len(x)

        #create X matrix
        X_matrix = np.zeros((m,l+1))
        if theta_init is not None:
            theta = theta_init
        else:
            theta = np.zeros(l+1)

        for i in range(m):
            for j in range(l+1):
                X_matrix[i,j] = x[i]**j

        X_matrix_T = X_matrix.T #transpose of X
        #print(X_matrix)

        #now do it`12
        k = 1
        kmax = 500
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
        print(k)
        return(store_theta, J)


    def Normal_Linear_Regression(x, y, l):
        m = len(x)
        assert m <1e4

        #create X matrix
        X_matrix = np.ones((m,l+1))
        for i in range(m):
            for j in range(1,l+1):
                X_matrix[i,j] = x[i]     
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


