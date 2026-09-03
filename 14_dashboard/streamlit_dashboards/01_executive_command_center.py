import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Executive Command Center", layout="wide")
data_file = Path(__file__).with_name("software_companies_dataset_v2.csv")
df = pd.read_csv(data_file)
df["Industry"] = df["Industry"].fillna("Unknown")
df["Employees"] = df["Employees"].fillna(df["Employees"].median())
df["Annual_Revenue"] = df["Annual_Revenue"].fillna(df["Annual_Revenue"].median())
df["Profit_Margin"] = df["Profit_Margin"].fillna(df["Profit_Margin"].median())
df["Profit_Estimate"] = df["Annual_Revenue"] * df["Profit_Margin"] / 100
df["Technology_Index"] = df[["Adoption_Rate_AI", "Adoption_Rate_Cloud",
                              "Adoption_Rate_Blockchain"]].mean(axis=1)

st.title("Executive Command Center")
st.caption("Portfolio-level performance, profitability and market-position analysis.")

with st.sidebar:
    countries = st.multiselect("Countries", sorted(df["Country"].dropna().unique()))
    industries = st.multiselect("Industries", sorted(df["Industry"].dropna().unique()))
    risks = st.multiselect("Risk ratings", sorted(df["Risk_Rating"].dropna().unique()))
    top_n = st.slider("Companies in ranking", 5, 30, 12)

view = df.copy()
if countries:
    view = view[view["Country"].isin(countries)]
if industries:
    view = view[view["Industry"].isin(industries)]
if risks:
    view = view[view["Risk_Rating"].isin(risks)]
if view.empty:
    st.warning("No records match the selected filters.")
    st.stop()

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Companies", f"{len(view):,}")
k2.metric("Revenue", f"${view['Annual_Revenue'].sum()/1e9:,.2f}B")
k3.metric("Estimated profit", f"${view['Profit_Estimate'].sum()/1e9:,.2f}B")
k4.metric("Employees", f"{view['Employees'].sum():,.0f}")
k5.metric("Technology index", f"{view['Technology_Index'].mean():.1f}")

tab1, tab2, tab3 = st.tabs(["Performance", "Market map", "Company ranking"])

with tab1:
    left, right = st.columns(2)
    by_industry = view.groupby("Industry", as_index=False).agg(
        Revenue=("Annual_Revenue", "sum"),
        Profit=("Profit_Estimate", "sum"),
        Companies=("Company_ID", "count")
    )
    left.plotly_chart(px.bar(by_industry.sort_values("Revenue"), x="Revenue", y="Industry",
                             orientation="h", color="Profit", title="Revenue and profit by industry"),
                      use_container_width=True)
    right.plotly_chart(px.scatter(view, x="Annual_Revenue", y="Profit_Margin",
                                  size="Employees", color="Risk_Rating",
                                  hover_name="Company_Name", log_x=True,
                                  title="Revenue–margin portfolio"),
                       use_container_width=True)

with tab2:
    market = view.groupby(["Country", "Industry"], as_index=False).agg(
        Revenue=("Annual_Revenue", "sum"), Market_Share=("Market_Share", "mean")
    )
    st.plotly_chart(px.treemap(market, path=["Country", "Industry"], values="Revenue",
                               color="Market_Share", title="Revenue concentration map"),
                    use_container_width=True)

with tab3:
    metric = st.selectbox("Ranking metric", ["Annual_Revenue", "Profit_Estimate",
                                              "Market_Share", "Technology_Index"])
    ranked = view.nlargest(top_n, metric)
    st.plotly_chart(px.bar(ranked.sort_values(metric), x=metric, y="Company_Name",
                           orientation="h", color="Industry",
                           title=f"Top {top_n} companies by {metric.replace('_', ' ')}"),
                    use_container_width=True)
    st.download_button("Download filtered data", view.to_csv(index=False),
                       "executive_filtered_companies.csv", "text/csv")
