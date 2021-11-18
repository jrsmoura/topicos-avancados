import joblib

def main():
    model = joblib.load('model_clf.pkl')
    print(model.predict([[5.5, 1.7]]))


if __name__ == '__main__':
    main()
