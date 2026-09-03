from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Company Performance", page_icon="📊", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    path = Path(__file__).with_name("software_companies_dataset.csv")
    data = pd.read_csv(path)
    data["Industry"] = data["Industry"].fillna("Unknown")
    data["Headquarters_City"] = data["Headquarters_City"].fillna("Unknown")
    return data


df = load_data()

st.title("📊 Software Company Performance Dashboard")
st.caption("Compare company scale, revenue, profitability, market share, and risk.")

with st.sidebar:
    st.header("Filters")
    countries = st.multiselect("Country", sorted(df["Country"].unique()))
    industries = st.multiselect("Industry", sorted(df["Industry"].unique()))
    risks = st.multiselect("Risk rating", sorted(df["Risk_Rating"].unique()))

filtered = df.copy()
if countries:
    filtered = filtered[filtered["Country"].isin(countries)]
if industries:
    filtered = filtered[filtered["Industry"].isin(industries)]
if risks:
    filtered = filtered[filtered["Risk_Rating"].isin(risks)]

if filtered.empty:
    st.warning("No companies match the selected filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Companies", f"{len(filtered):,}")
c2.metric("Total revenue", f"${filtered['Annual_Revenue'].sum() / 1_000_000:,.1f}M")
c3.metric("Average profit margin", f"{filtered['Profit_Margin'].mean():.1f}%")
c4.metric("Total employees", f"{filtered['Employees'].sum():,.0f}")

left, right = st.columns(2)
with left:
    revenue_by_industry = (
        filtered.groupby("Industry", as_index=False)["Annual_Revenue"]
        .sum()
        .sort_values("Annual_Revenue", ascending=False)
    )
    fig = px.bar(
        revenue_by_industry,
        x="Industry",
        y="Annual_Revenue",
        title="Total Revenue by Industry",
        labels={"Annual_Revenue": "Revenue ($)"},
        color="Annual_Revenue",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.scatter(
        filtered,
        x="Employees",
        y="Annual_Revenue",
        color="Risk_Rating",
        size="Market_Share",
        hover_name="Company_Name",
        title="Employees vs Annual Revenue",
        labels={"Annual_Revenue": "Revenue ($)"},
    )
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    risk_counts = filtered["Risk_Rating"].value_counts().rename_axis("Risk").reset_index(name="Companies")
    fig = px.pie(risk_counts, names="Risk", values="Companies", hole=0.45, title="Risk Rating Distribution")
    st.plotly_chart(fig, use_container_width=True)

with right:
    profit_by_country = (
        filtered.groupby("Country", as_index=False)["Profit_Margin"]
        .mean()
        .sort_values("Profit_Margin", ascending=False)
    )
    fig = px.bar(
        profit_by_country,
        x="Country",
        y="Profit_Margin",
        title="Average Profit Margin by Country",
        labels={"Profit_Margin": "Average profit margin (%)"},
        color="Profit_Margin",
        color_continuous_scale="Greens",
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Companies by Revenue")
top = filtered.nlargest(10, "Annual_Revenue")[[
    "Company_Name", "Industry", "Country", "Risk_Rating", "Employees",
    "Annual_Revenue", "Profit_Margin", "Market_Share"
]]
st.dataframe(
    top.style.format({
        "Employees": "{:,.0f}",
        "Annual_Revenue": "${:,.2f}",
        "Profit_Margin": "{:.2f}%",
        "Market_Share": "{:.2f}%",
    }),
    use_container_width=True,
    hide_index=True,
)

