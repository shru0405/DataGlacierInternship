import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

data = pd.read_csv(r"C:\Users\shrut\Desktop\Data Glacier Stuff\Algorithms\Clean_file.csv")
data.head()

subset = data.iloc[:,:20]

for col in subset.columns:
    print(col)
    print(subset[col].nunique())

    data.drop('Ptid', axis=1, inplace=True)
    data['Persistency_Flag'].replace({'Persistent': 1, 'Non-Persistent': -1}, inplace=True)
    data = pd.get_dummies(data)

    data.head()
    data.dtypes
    data['Persistency_Flag'].value_counts()
    data.shape
    X = data.drop('Persistency_Flag', axis=1)
    y = data['Persistency_Flag']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, shuffle=True)

    model = SVC(kernel='linear', random_state=123)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f'Accuracy upon the test data is {100 * accuracy:.2f} %')