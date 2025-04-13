
#  Salary Predictor - Multiple Regression App

This project is a modularized Python application that trains a **multiple linear regression model** to predict salaries based on **experience**, **education level**, and **age**. It also includes a **Streamlit web app** that allows users to input values and receive a real-time salary prediction.

---

## Project Structure

```
multiple_regression_project/
├── app.py                       # Streamlit app for user input and prediction
├── main.py                      # Script to load data, train, and save the model
├── data/
│   └── dataset.csv              # Sample training dataset
├── models/
│   └── regression_model.py      # Contains training, saving, loading, and prediction logic
├── utils/
│   └── data_loader.py           # Loads the dataset from CSV
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Features

- Train a multiple linear regression model using custom data
- Modular codebase with separate concerns (data, model, UI)
- Streamlit interface for interactive predictions
- Input fields for:
  - Years of experience
  - Education level (1–5 scale)
  - Age
- Displays predicted salary in real-time

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multiple-regression-app.git
cd multiple-regression-app
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Script ACtivate          # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Run the training script to build and save the regression model:

```bash
python main.py
```

You should see:
```
Model saved successfully.
```

### 5. Launch the Streamlit App

```bash
streamlit run app.py
```

The app should open in your browser at `http://localhost:8501`.

---

## Sample Dataset Format

Make sure your dataset (`data/dataset.csv`) includes the following columns:

```csv
Experience,Education_Level,Age,Salary
2,3,25,45000
5,4,30,60000
10,5,40,90000
...
```

- `Education_Level` should be an integer from 1 (High School) to 5 (PhD).

---

## Requirements

```
streamlit
pandas
scikit-learn
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Upload CSV for bulk prediction
- Visualization of predicted salary range
- Confidence intervals and model accuracy display
- Save prediction logs

---

## Author

Developed by [Your Name]  


---

## License

This project is licensed under the MIT License.
