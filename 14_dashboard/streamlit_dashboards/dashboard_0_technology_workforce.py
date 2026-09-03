from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Technology & Workforce", page_icon="🤖", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    path = Path(__file__).with_name("software_companies_dataset.csv")
    data = pd.read_csv(path)
    data["Industry"] = data["Industry"].fillna("Unknown")
    data["Primary_Cloud"] = data["Primary_Cloud"].fillna("Unknown")
    return data


df = load_data()

st.title("🤖 Technology Adoption & Workforce Dashboard")
st.caption("Explore technology adoption, R&D investment, employee training, and satisfaction.")

with st.sidebar:
    st.header("Filters")
    industries = st.multiselect("Industry", sorted(df["Industry"].unique()))
    ownership = st.multiselect("Ownership type", sorted(df["Ownership_Type"].unique()))
    clouds = st.multiselect("Primary cloud", sorted(df["Primary_Cloud"].unique()))
    min_ai = st.slider("Minimum AI adoption (%)", 0, 100, 0)

filtered = df.copy()
if industries:
    filtered = filtered[filtered["Industry"].isin(industries)]
if ownership:
    filtered = filtered[filtered["Ownership_Type"].isin(ownership)]
if clouds:
    filtered = filtered[filtered["Primary_Cloud"].isin(clouds)]
filtered = filtered[filtered["Adoption_Rate_AI"] >= min_ai]

if filtered.empty:
    st.warning("No companies match the selected filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Average AI adoption", f"{filtered['Adoption_Rate_AI'].mean():.1f}%")
c2.metric("Average cloud adoption", f"{filtered['Adoption_Rate_Cloud'].mean():.1f}%")
c3.metric("Average training hours", f"{filtered['Training_Hours_Per_Employee'].mean():.1f}")
c4.metric("Employee satisfaction", f"{filtered['Employee_Satisfaction'].mean():.2f}/5")

adoption = (
    filtered.groupby("Industry")[["Adoption_Rate_AI", "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain"]]
    .mean()
    .reset_index()
    .melt(id_vars="Industry", var_name="Technology", value_name="Adoption Rate")
)
adoption["Technology"] = adoption["Technology"].replace({
    "Adoption_Rate_AI": "AI",
    "Adoption_Rate_Cloud": "Cloud",
    "Adoption_Rate_Blockchain": "Blockchain",
})
fig = px.bar(
    adoption,
    x="Industry",
    y="Adoption Rate",
    color="Technology",
    barmode="group",
    title="Average Technology Adoption by Industry",
    labels={"Adoption Rate": "Adoption rate (%)"},
)
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    fig = px.scatter(
        filtered,
        x="Training_Hours_Per_Employee",
        y="Employee_Satisfaction",
        color="Ownership_Type",
        size="Employees",
        hover_name="Company_Name",
        title="Training Hours vs Employee Satisfaction",
        labels={
            "Training_Hours_Per_Employee": "Training hours per employee",
            "Employee_Satisfaction": "Satisfaction score",
        },
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.scatter(
        filtered,
        x="R&D_Spending",
        y="Adoption_Rate_AI",
        color="Primary_Cloud",
        hover_name="Company_Name",
        title="R&D Spending vs AI Adoption",
        labels={"R&D_Spending": "R&D spending ($)", "Adoption_Rate_AI": "AI adoption (%)"},
    )
    st.plotly_chart(fig, use_container_width=True)

cloud_counts = filtered["Primary_Cloud"].value_counts().rename_axis("Cloud").reset_index(name="Companies")
fig = px.bar(
    cloud_counts,
    x="Cloud",
    y="Companies",
    color="Companies",
    title="Primary Cloud Platform Distribution",
    color_continuous_scale="Purples",
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Technology Leaders")
leaders = filtered.nlargest(10, "Adoption_Rate_AI")[[
    "Company_Name", "Industry", "Primary_Cloud", "Adoption_Rate_AI",
    "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain", "R&D_Spending",
    "Training_Hours_Per_Employee", "Employee_Satisfaction"
]]
st.dataframe(
    leaders.style.format({
        "Adoption_Rate_AI": "{:.2f}%",
        "Adoption_Rate_Cloud": "{:.2f}%",
        "Adoption_Rate_Blockchain": "{:.2f}%",
        "R&D_Spending": "${:,.2f}",
        "Training_Hours_Per_Employee": "{:.1f}",
        "Employee_Satisfaction": "{:.2f}",
    }),
    use_container_width=True,
    hide_index=True,
)

