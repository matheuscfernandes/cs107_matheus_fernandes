from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression,RidgeRegression 

dataset = datasets.load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alpha = 0.1
LRModel=LinearRegression()
LRModel.set_params(beta=1)

RRModel=RidgeRegression()
RRModel.set_params(beta=1,alpha=alpha)

models = [LRModel,RRModel]

err=[]
for model in models:
    model.fit(X_train, y_train);
    err.append(model.score(X_test,y_test))