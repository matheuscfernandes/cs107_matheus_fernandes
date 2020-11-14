from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

#train and score the LinearRegression class object
lr_model = reg.LinearRegression();
lr_model.fit(X_train, y_train);
print(lr_model); #print model repr
print("R^2=", lr_model.score(X_test, y_test)); #score on test data
print( lr_model.get_params() );
print()


alpha = 0.1
#train and score the RidgeRegression class object
rr_model = reg.RidgeRegression();
print(rr_model);
#fit rr_model using fit_1, which penalizes the intercept and uses just alpha as the penalty
print("Fitting RidgeRegression model that penalizes intercept and uses just alpha for penalty.");
rr_model.fit_1(X_train, y_train);
print("R^2=", rr_model.score(X_test, y_test)); #score on test data