from pathlib import Path
import pickle

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Annual Revenue Predictor",
    page_icon="📈",
    layout="centered",
)

st.title("Software Company Annual Revenue Predictor")
st.write("Enter the company details to predict its annual revenue.")

# Load the directly pickled LinearRegression model
model_path = Path(__file__).with_name("annual_revenue_model.pkl")

if not model_path.exists():
    st.error(
        "annual_revenue_model.pkl was not found. Keep the pickle file "
        "in the same folder as this dashboard file."
    )
    st.stop()

with model_path.open("rb") as file:
    model = pickle.load(file)

# The feature order must be the same as the training notebook
features = [
    "Employees",
    "Market_Share",
    "Profit_Margin",
    "Adoption_Rate_AI",
    "Adoption_Rate_Cloud",
]

st.subheader("Enter Company Details")

employees = st.number_input(
    "Number of Employees",
    min_value=0,
    value=5000,
    step=100,
)

market_share = st.number_input(
    "Market Share",
    min_value=0.0,
    value=8.5,
    step=0.1,
)

profit_margin = st.number_input(
    "Profit Margin",
    value=18.0,
    step=0.1,
)

ai_adoption = st.number_input(
    "AI Adoption Rate",
    min_value=0.0,
    value=75.0,
    step=1.0,
)

cloud_adoption = st.number_input(
    "Cloud Adoption Rate",
    min_value=0.0,
    value=85.0,
    step=1.0,
)

# Create one prediction record
input_data = pd.DataFrame(
    {
        "Employees": [employees],
        "Market_Share": [market_share],
        "Profit_Margin": [profit_margin],
        "Adoption_Rate_AI": [ai_adoption],
        "Adoption_Rate_Cloud": [cloud_adoption],
    }
)

input_data = input_data[features]

if st.button("Predict Annual Revenue", type="primary"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Annual Revenue: {prediction:,.2f}")

    with st.expander("View Input Data"):
        st.dataframe(input_data, use_container_width=True)
