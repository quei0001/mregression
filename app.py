import streamlit as st
from models.regression_model import load_model, predict_salary

st.set_page_config(page_title="Salary Predictor", layout="centered")

# Load the model
try:
    model = load_model('models/linear_regression_model.pkl')
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Streamlit UI
st.title("💼 Salary Predictor")
st.write("Enter your details to estimate your salary:")

experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
education_level = st.slider("Education Level (1 = High School, 5 = PhD)", 1, 5, 3)
age = st.number_input("Age", min_value=18, max_value=70, value=30)

if st.button("Predict Salary"):
    try:
        salary = predict_salary(model, experience, education_level, age)
        st.success(f"💰 Estimated Salary: **${salary:,.2f}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
