import numpy as np

class Regression():

    def __init__(self):
        self.params={}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError

class LinearRegression(Regression):
    def set_params(self, **kwargs):
        #assert to make sure the parameters exist in this implementation
        assert all([x in ['beta'] for x in kwargs.keys()]), 'argument not implemented'
        #set the params variable to the dictionary passed in 
        self.params=kwargs

    def fit(self,X,y):
        #converting incomind data into nuumpy arrays
        X=np.array(X)
        y=np.array(y)
        #add a column of ones for the bias
        X = np.hstack((np.ones([X.shape[0],1]), X))
        #solving for betas
        beta = np.dot(np.linalg.pinv(np.dot(X.T,X)),np.dot(X.T,y))
        self.params['beta']=beta
    
    def predict(self,X):
        #converting incomind data into nuumpy arrays
        X=np.array(X)
        #add a column of ones for the bias
        X = np.hstack((np.ones([X.shape[0],1]), X))
        #predicting based on the inputs and betas from previous fit
        y_hat = np.dot(X,self.params['beta'])
        return y_hat
    
    def score(self, X, y):
        #computing sst equation for r2
        sst=np.sum((y-np.mean(y))**2)
        #obtaning predictions from model
        y_hat=self.predict(X)
        #computing sse equation for r2
        sse=np.sum((y-y_hat)**2)
        #computing r2
        r2=1-sse/sst
        return r2

class RidgeRegression(LinearRegression):
    def set_params(self, **kwargs):
        #assert to make sure the parameters exist in this implementation
        assert all([x in ['beta','alpha'] for x in kwargs.keys()]), 'argument not implemented'
        #set the params variable to the dictionary passed in 
        self.params=kwargs

    def fit(self,X,y):
        #converting incomind data into nuumpy arrays
        X=np.array(X)
        y=np.array(y)
        #add a column of ones for the bias
        X = np.hstack((np.ones([X.shape[0],1]), X))
        #initializing gamma
        gamma = self.params['alpha']*np.identity(X.shape[1])
        #solving for beta
        beta = np.dot(np.linalg.pinv(np.dot(X.T,X)+np.dot(gamma.T,gamma)),np.dot(X.T,y))
        self.params['beta']=beta