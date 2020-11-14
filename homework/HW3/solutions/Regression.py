import numpy as np

class Regression():
    
    def __init__(self):
        self.params = dict()
        
    def get_params(self):
        return self.params
    
    def set_params(self, **kwargs):
        for key in kwargs:
            self.params[key] = kwargs[key]
        #OR
        #raise NotImplementedError;
    
    def fit(self, X, y):
        raise NotImplementedError;
    
    def predict(self, X):
        raise NotImplementedError;
    
    def score(self, X, y):
        raise NotImplementedError;

class LinearRegression(Regression):
    
    def __init__(self):
        super(LinearRegression, self).__init__()
    
    
    def fit(self, X, y):
        X = np.append(np.ones((X.shape[0], 1)), X, axis=1)
        beta = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(y)
        
        self.params['coef'] = beta[1:]
        self.params['intercept'] = beta[0]
    
    def predict(self, X):
        return np.dot(X, self.params['coef'])+self.params['intercept']

    def score(self, X, y):
        y_hat = self.predict(X)
        y_bar = np.mean(y)
        SST = np.sum((y - y_bar)**2)
        SSRes = np.sum((y_hat - y)**2)
        R2 = 1 - SSRes / SST
        return R2

    # Optional REPL Method.
    def __str__(self):
        return "LinearRegression"

class RidgeRegression(LinearRegression):
    
    def __init__(self, alpha=0.1):
        super(RidgeRegression, self).__init__()
        self.params['alpha'] = alpha

    #this version penalizes the intercept and uses a single alpha
    def fit_1(self, X, y):
        X = np.append(np.ones((X.shape[0], 1)), X, axis=1)
        C = X.T.dot(X) + self.params['alpha']*np.eye(X.shape[1]) #alpha*I
        beta = np.linalg.pinv(C).dot(X.T.dot(y))
#         print ("BETA SHAPE")
#         print (beta.shape)
        self.params['coef'] = beta[1:]
        self.params['intercept'] = beta[0]
        # print (self.params['coef'].shape )
        # print (self.params['intercept'].shape )
        
    #This fit solution also penalizes the intercept using alpha^2, which is consistent with the formula that we provided.
    def fit_2(self, X, y):
        X = np.append(np.ones((X.shape[0], 1)), X, axis=1);
        
        gamma = self.params['alpha']*np.eye(X.shape[1]); #define gamma
        C = X.T.dot(X) + gamma.T.dot(gamma); #gamma.T.dot(gamma) == alpha^2*I
        
        beta = np.linalg.pinv(C).dot(X.T.dot(y))
#         print ("BETA SHAPE")
#         print (beta.shape)
        self.params['coef'] = beta[1:];
        self.params['intercept'] = beta[0];


    # SKLEARN FIT IMPLEMENTATION does not penalize intercept and uses just alpha*I.
    def fit_sklearn_1(self, X, y):
        X_mean = np.mean(X, axis=0)
        y_mean = np.mean(y, axis=0)
        X_ = X - X_mean
        y_ = y - y_mean
                
        C = X_.T.dot(X_) + self.params['alpha']*np.eye(X_.shape[1]); #alpha*I
        coef = np.linalg.inv(C).dot(X_.T.dot(y_))
        intercept = y_mean - X_mean.dot(coef)
        self.params['coef'] = coef
        self.params['intercept'] = intercept
        
    # SKLEARN FIT IMPLEMENTATION does not penalize intercept and uses alpha^2, which is consistent with our formula.
    def fit_sklearn_2(self, X, y):
        X_mean = np.mean(X, axis=0)
        y_mean = np.mean(y, axis=0)
        X_ = X - X_mean
        y_ = y - y_mean
        
        gamma = self.params['alpha']*np.eye(X.shape[1]); #define gamma
        C = X_.T.dot(X_) + gamma.T.dot(gamma); #gamma.T.dot(gamma) == alpha^2*I
        
        coef = np.linalg.inv(C).dot(X_.T.dot(y_))
        intercept = y_mean - X_mean.dot(coef)
        self.params['coef'] = coef
        self.params['intercept'] = intercept
        
    # Optional REPL Method. Does NOT count for grading
    def __str__(self):
        return "RidgeRegression"