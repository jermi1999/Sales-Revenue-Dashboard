import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Sales & Revenue Analysis Dashboard")

df = pd.read_csv("sales_data.csv")

st.write("Dataset Preview")
st.dataframe(df)

total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()

st.metric("Total Sales", total_sales)
st.metric("Total Revenue", f"₹{total_revenue}")

sales_chart = px.bar(
    df,
    x="Product",
    y="Sales",
    title="Product-wise Sales"
)

revenue_chart = px.pie(
    df,
    names="Product",
    values="Revenue",
    title="Revenue Distribution"
)

st.plotly_chart(sales_chart)
st.plotly_chart(revenue_chart)