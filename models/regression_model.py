import pickle
from sklearn.linear_model import LinearRegression

def train_model(X, y, model_path='models/linear_regression_model.pkl'):
    model = LinearRegression()
    model.fit(X, y)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print("Model saved successfully.")
    return model

def load_model(model_path='models/linear_regression_model.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_salary(model, experience, education_level, age):
    features = [[experience, education_level, age]]
    return model.predict(features)[0]
