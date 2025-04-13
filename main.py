from utils.data_loader import load_data, split_data
from models.regression_model import train_model, evaluate_model, save_model

def main():
    # Load and split data
    X, y = load_data('data/dataset.csv')
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    mse, r2, predictions = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Save model
    save_model(model)
    print("Model saved successfully.")

if __name__ == '__main__':
    main()
