from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg 
import numpy as np
import matplotlib.pyplot as plt

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


scoreRR=[]
scoreLR=[]

LRModel=reg.LinearRegression()
LRModel.set_params()
LRModel.fit(X_train, y_train);
score=LRModel.score(X_test,y_test)

RRModel=reg.RidgeRegression()

for alpha in 10**np.linspace(-2,1,15):
    RRModel.set_params(alpha=alpha)
    RRModel.fit(X_train, y_train);
    scoreRR.append([alpha,RRModel.score(X_test,y_test)])
    scoreLR.append([alpha,score])

scoreRR=np.array(scoreRR)
scoreLR=np.array(scoreLR)

plt.semilogx(scoreRR[:,0],scoreRR[:,1],'o-',label='Ridge Regression')
plt.semilogx(scoreLR[:,0],scoreLR[:,1],'o-',label='Linear Regression')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$R^2$ score')
plt.legend()
plt.savefig('P2F.png',format='png',dpi=300)
plt.show()