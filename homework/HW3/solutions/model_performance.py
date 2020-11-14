from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

from Regression import LinearRegression
from Regression import RidgeRegression

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

lines = np.zeros((3, 10, 2))
alpha = 0.1

models = [LinearRegression(),
      RidgeRegression(alpha)]

for id, alpha in enumerate(np.linspace(0.05, 1, 10)): # 1 point for using at least 10 values of alpha

    for num, model in enumerate(models):
        model.set_params(alpha=alpha); # 1 point for using set_params to adjust alpha
        if num == 1:
            model.fit_sklearn_1(X_train, y_train);
        else:
            model.fit(X_train, y_train)
        lines[num, id] = [model.score(X_test, y_test), alpha]

# 3 points for correct and labeled plot
plt.xlabel("alpha value")
plt.ylabel("$R^2$ Score")
plt.ylim(0.66,0.67)

for i, line in enumerate(lines):
    plt.plot(line[:,1], line[:,0])
plt.legend(["Linear Regression", "Ridge Regression"], bbox_to_anchor=(0.5, 0.5))
# plt.show();
plt.savefig('P2F.png');