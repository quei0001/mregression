import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    data = pd.read_csv(filepath)
    X = data[['Experience', 'Education_Level', 'Age']]
    y = data['Salary']
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
