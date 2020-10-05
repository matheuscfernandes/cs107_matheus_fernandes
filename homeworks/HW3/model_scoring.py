from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


alpha = 0.1
#initialize LR model
LRModel=reg.LinearRegression()

#initilizse the RR model
RRModel=reg.RidgeRegression()
RRModel.set_params(alpha=alpha)

#put both models into a list 
models = [LRModel,RRModel]

#initialize empty list to store the scores of the models
score=[]

#iterate over the models
for model in models:
    model.fit(X_train, y_train);
    score.append(model.score(X_test,y_test))

#print the computed scores for the different models in nice format
print('LRModel R2 Score: {}\nRRModel R2 Score: {}'.format(score[0],score[1]))