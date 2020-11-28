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