import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Finance Forecast App", layout="wide")

st.title("📊 Financial Forecast & Break-Even Analysis")

# File Upload
uploaded_file = st.file_uploader("📁 Upload Financial Data (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Handle Excel or CSV
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        sheets = pd.read_excel(uploaded_file, sheet_name=None)
        sheet = st.selectbox("Select Sheet", list(sheets.keys()))
        df = sheets[sheet]

    st.subheader("📂 Uploaded Data Preview")
    st.dataframe(df.head())

    st.success("✅ File loaded successfully. Start configuring your forecast.")
    
    # Placeholder summary
    st.markdown("## 🔍 Forecast Modules (auto-generated)")
    st.markdown("""
    - 📆 **Pro Forma Reports**: Monthly, Quarterly, Yearly  
    - 💸 **Burn Rate + Funding Forecast**  
    - 📈 **Break-even Analysis** (Operational, Cash Flow, Investment Recovery)  
    - 🔁 **Sensitivity Analysis** (Conservative, Base, Optimistic, Pessimistic)  
    - 📤 **Export** results to Excel or PDF  
    """)

    st.info("Coming next: data mapping, forecast logic, export buttons.")

else:
    st.warning("⚠️ Upload your Excel or CSV file to get started.")
