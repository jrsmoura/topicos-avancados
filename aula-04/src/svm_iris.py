from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import numpy as np
import matplotlib.pyplot as plt
import joblib


def main():
    iris = load_iris()

    X = iris.data[:, (2, 3)]
    y = (iris.target==2).astype(np.float32)

    svm_clf = Pipeline([
        ('scaler', StandardScaler()), 
        ('linear_svc', LinearSVC(C=1, loss='hinge'))
        ])
    svm_clf.fit(X, y)
    joblib.dump(svm_clf, 'model_clf.pkl')
    print(svm_clf.predict([[5., 1.7]])) # 1.
    print(svm_clf.predict([[1., 0.1]])) # 0.
    

if __name__ == '__main__':
    main()

