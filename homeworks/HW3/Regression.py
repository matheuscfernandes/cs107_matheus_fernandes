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
        assert all([x in ['beta','alpha'] for x in kwargs.keys()]), 'argument not implemented'
        #set the params variable to the dictionary passed in 
        self.params=kwargs
        print (self.params)

    def fit(self,X,y):
        #converting incomind data into nuumpy arrays
        X=np.array(X)
        y=np.array(y)
        #add a column of ones for the bias
        X = np.hstack((np.ones([X.shape[0],1]), X))
        #solving for betas
        beta = np.dot(np.linalg.pinv(np.dot(X.T,X)),np.dot(X.T,y))
        self.params['beta']=beta
    
    # def predict(self,X):




test=LinearRegression()
test.set_params(beta=[1,2,3],alpha=[1,1])
