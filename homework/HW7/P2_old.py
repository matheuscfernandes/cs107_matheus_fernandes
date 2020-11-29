import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
               id, 
               desc TEXT, 
               param_name TEXT, 
               value TEXT )''')

cursor.execute('''CREATE TABLE model_coefs (
               id, 
               desc TEXT, 
               feature_name TEXT, 
               value FLOAT )''')

cursor.execute('''CREATE TABLE model_results (
               id, 
               desc TEXT, 
               train_score FLOAT, 
               test_score FLOAT )''')


def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    model_params = model.get_params()
    model_coefs = model.intercept_
    model_coefs = np.append(model_coefs, model.coef_) #remember to deal with intercept too
    # adding to params
    for key, value in model_params.items():
        cursor.execute('''INSERT INTO model_params (id, desc, param_name, value) 
        VALUES (?, ?, ?, ?)''', (model_id,model_desc, key, value))
    #making list of features
    feature_name = ['Intercept']
    for cols in X_train.columns:
        feature_name.append(cols)
    #adding features and names
    for coef,feature in zip(model_coefs, feature_name):
        #iterating feature name
        cursor.execute('''INSERT INTO model_coefs(id, desc, feature_name, value) 
        VALUES (?, ?, ?,?)''', (model_id, model_desc, feature, coef))

    cursor.execute('''INSERT INTO model_results(id,desc, train_score, test_score) 
        VALUES (?, ?, ?,?)''', (model_id, model_desc, train_score, test_score))

baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

#first model
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

# adding second column:
feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

#second model
save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

#3rd model
save_to_database(3, 'L1 penalty mode', db, penalized_model, X_train, X_test, y_train, y_test)

#getting best model and id
cursor.execute("SELECT id, MAX(test_score) FROM model_results")
best_fetch = cursor.fetchall()
best_id = best_fetch[0][0]
best_score = best_fetch[0][1]

print(f"Best model id: {best_id}")
print(f"Best validation score: {best_score:.4f}")

#getting features of best model
cursor.execute(f"SELECT feature_name, value FROM model_coefs WHERE id={best_id}")
coefficients = cursor.fetchall()
coef_vals = np.array([])
for coef in coefficients:
    print(f"{coef[0]}: {coef[1]}")
    coef_vals = np.append(coef_vals,coef[1])


test_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
test_model.fit(X_train, y_train)

# Manually change fit parameters

test_model.coef_ = np.array([coef_vals[1:]])
test_model.intercept_ = np.array([coef_vals[0]])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.commit()
db.close()