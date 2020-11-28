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
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               param_name TEXT, 
               value REAL)''')

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               feature_name TEXT, 
               value REAL)''')

cursor.execute('''CREATE TABLE model_results (
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               train_score REAL, 
               test_score REAL)''')

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
    feature_names=list(X_train.keys())
    cursor = db.cursor()
    print(train_score,test_score,feature_names)

    cursor = db.cursor()
    vals_to_insert = (int(model_id), first_name, last_name, middle_name, party)
    cursor.execute('''INSERT INTO candidates 
                    (id, first_name, last_name, middle_init, party)
                    VALUES (?, ?, ?, ?, ?)''', vals_to_insert)
    db.commit()


# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

save_to_database(1,'Baseline model', db, baseline_model,X_train,X_test,y_train,y_test)






def viz_tables(cols, query):
    q = cursor.execute(query).fetchall()
    framelist = dict()
    for i, col_name in enumerate(cols):
        framelist[col_name] = [row[i] for row in q]
    return pd.DataFrame.from_dict(framelist)


viz_tables(candidate_cols, query)