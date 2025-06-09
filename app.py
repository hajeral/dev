import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Financial Forecast & Break-Even")

st.sidebar.header("Input Financials")

capex = st.sidebar.number_input("Total CapEx ($)", value=2140000)
salary_q = st.sidebar.number_input("Quarterly Salary ($)", value=250000)
opex_q = st.sidebar.number_input("Quarterly OpEx ($)", value=100000)
revenue_q = st.sidebar.number_input("Quarterly Revenue ($)", value=600000)

quarters = [f"Q{i+1} Y1" for i in range(4)]
df = pd.DataFrame({
    "Quarter": quarters,
    "Revenue": [revenue_q]*4,
    "Salary": [salary_q]*4,
    "OPEX": [opex_q]*4,
    "CAPEX": [capex/4]*4
})
df["Total Cost"] = df["Salary"] + df["OPEX"] + df["CAPEX"]
df["Net Profit"] = df["Revenue"] - df["Total Cost"]
df["Cumulative Profit"] = df["Net Profit"].cumsum()

st.subheader("📈 Financial Table")
st.dataframe(df)

breakeven = df[df["Cumulative Profit"] > 0].head(1)
if not breakeven.empty:
    st.success(f"🎯 Break-even in: {breakeven['Quarter'].values[0]}")
else:
    st.warning("Break-even not reached.")
