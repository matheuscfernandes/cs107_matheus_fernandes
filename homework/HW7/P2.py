import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")


cursor.execute('''CREATE TABLE model_params (
               id, 
               desc TEXT, 
               param_name TEXT, 
               value REAL)''')

cursor.execute('''CREATE TABLE model_coefs (
               id, 
               desc TEXT, 
               feature_name TEXT, 
               value FLOAT)''')

cursor.execute('''CREATE TABLE model_results (
               id, 
               desc TEXT, 
               train_score FLOAT, 
               test_score FLOAT)''')

db.commit() # Commit changes to the database


# Load data
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

def save_to_database(model_id,model_desc,db,model,X_train,X_test,y_train,y_test):
    train_score=model.score(X_train,y_train)
    test_score=model.score(X_test,y_test)
    model_coefs = np.append(model.intercept_,model.coef_)
    param_names=['Intercept']+list(X_train.keys())

    cursor = db.cursor()
    for key,values in model.get_params().items():
        cursor.execute('''INSERT INTO model_params 
                        (id, desc, param_name, value)
                        VALUES (?, ?, ?, ?)''', (int(model_id), model_desc, key, values))
    for param, coefs in zip(param_names,model_coefs):
        cursor.execute('''INSERT INTO model_coefs 
                        (id, desc, feature_name, value)
                        VALUES (?, ?, ?, ?)''', (int(model_id), model_desc, param, coefs))
    cursor.execute('''INSERT INTO model_results 
                    (id, desc, train_score, test_score)
                    VALUES (?, ?, ?, ?)''', (int(model_id), model_desc, train_score, test_score))
    db.commit()




# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

save_to_database(1,'Baseline model', db, baseline_model,X_train,X_test,y_train,y_test)


feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

save_to_database(2,'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

save_to_database(3,'L1 penalty model', db, penalized_model,X_train,X_test,y_train,y_test)


# PART C
#### still to do __________________________________
query = "SELECT id, desc ,MAX(test_score) FROM model_results"
cursor.execute(query)
best = cursor.fetchall()
id = best[0][0]
desc = best[0][1]
best_score = best[0][2]

print(f'Best model is #{id} ({desc}) with test score {best_score}')

cursor.execute(f"SELECT feature_name, value FROM model_coefs WHERE id={id}")
coefs = np.array(cursor.fetchall())

intercept=np.array(coefs[0,1],dtype=float)
coef=np.array(coefs[1:,1],dtype=float)

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')



# def viz_tables(cols, query):
#     q = cursor.execute(query).fetchall()
#     framelist = dict()
#     for i, col_name in enumerate(cols):
#         framelist[col_name] = [row[i] for row in q]
#     return pd.DataFrame.from_dict(framelist)

# model_params_cols=['id', 'desc', 'param_name', 'value']
# query = '''SELECT * FROM model_params'''
# print(viz_tables(model_params_cols, query))

# model_coef_cols=['id', 'desc', 'feature_name', 'value']
# query = '''SELECT * FROM model_coefs'''
# print(viz_tables(model_coef_cols, query))

# model_results_cols=['id', 'desc', 'train_score', 'test_score']
# query = '''SELECT * FROM model_results'''
# print(viz_tables(model_results_cols, query))


db.close()