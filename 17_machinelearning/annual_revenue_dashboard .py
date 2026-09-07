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
st.write(
    "Enter the company details below. The trained multiple linear regression "
    "model will estimate its annual revenue."
)

model_path = Path(__file__).with_name("annual_revenue_model.pkl")

if not model_path.exists():
    st.error(
        "annual_revenue_model.pkl was not found. Run all cells in the training "
        "notebook first and keep the generated pickle file in this folder."
    )
    st.stop()

with model_path.open("rb") as file:
    model_bundle = pickle.load(file)

model = model_bundle["model"]
features = model_bundle["features"]

st.subheader("Company information")

employees = st.number_input(
    "Number of employees",
    min_value=0,
    value=5000,
    step=100,
)
market_share = st.number_input(
    "Market share",
    min_value=0.0,
    value=8.5,
    step=0.1,
)
profit_margin = st.number_input(
    "Profit margin",
    value=18.0,
    step=0.1,
)
ai_adoption = st.number_input(
    "AI adoption rate",
    min_value=0.0,
    value=75.0,
    step=1.0,
)
cloud_adoption = st.number_input(
    "Cloud adoption rate",
    min_value=0.0,
    value=85.0,
    step=1.0,
)

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
    predicted_revenue = model.predict(input_data)[0]
    st.success(f"Predicted Annual Revenue: {predicted_revenue:,.2f}")

    with st.expander("View input data"):
        st.dataframe(input_data, use_container_width=True)
