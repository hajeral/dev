import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Financial Forecast App")

st.title("📊 Financial Forecast & Break-Even Analysis")

# Sidebar Inputs
st.sidebar.header("💰 Input Assumptions")

capex = st.sidebar.number_input("Total CapEx (one-time)", value=2140000, step=10000)
salary_q = st.sidebar.number_input("Quarterly Salary Expense", value=250000, step=10000)
opex_q = st.sidebar.number_input("Quarterly Operating Expense", value=100000, step=5000)
revenue_q = st.sidebar.number_input("Quarterly Revenue (Start)", value=600000, step=10000)
growth_rate = st.sidebar.slider("Quarterly Revenue Growth Rate (%)", 0, 100, 20)

# Generate data for 12 quarters (3 years)
quarters = [f"Q{(i%4)+1} Y{(i//4)+1}" for i in range(12)]
revenues = [revenue_q * ((1 + growth_rate/100) ** i) for i in range(12)]
salary_exp = [salary_q]*12
opex_exp = [opex_q]*12
capex_exp = [capex if i == 0 else 0 for i in range(12)]

# Create DataFrame
df = pd.DataFrame({
    "Quarter": quarters,
    "Revenue": revenues,
    "Salaries": salary_exp,
    "OPEX": opex_exp,
    "CAPEX": capex_exp
})

df["Total Cost"] = df["Salaries"] + df["OPEX"] + df["CAPEX"]
df["Net Profit"] = df["Revenue"] - df["Total Cost"]
df["Cumulative Profit"] = df["Net Profit"].cumsum()

# Display Results
st.subheader("📈 Forecast Table")
numeric_cols = df.select_dtypes(include='number').columns
st.dataframe(df.style.format({col: "${:,.0f}" for col in numeric_cols}))

# Break-even
breakeven = df[df["Cumulative Profit"] > 0]
if not breakeven.empty:
    st.success(f"🎯 Break-even reached in: **{breakeven.iloc[0]['Quarter']}**")
else:
    st.warning("❌ Break-even not reached within 3 years.")

