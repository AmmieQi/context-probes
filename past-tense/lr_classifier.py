import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/elmo_sen_train.csv", header=None)
X_train = df.loc[:, :1023] #first 512 columns are embeddings
Y_train = df.loc[:, 1024] #last column is class label

df = pd.read_csv("data/elmo_sen_test.csv", header=None)
X_test = df.loc[:, :1023] #first 512 columns are embeddings
Y_test = df.loc[:, 1024] #last column is class label

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20)

## Use Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, Y_train)
print(lr.score(X_test, Y_test))
