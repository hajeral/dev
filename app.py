
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial Forecast", layout="wide")
st.title("📊 Financial Forecasting Tool")

uploaded_file = st.file_uploader("Upload your Excel file (with multiple sheets)", type=["xlsx"])

if uploaded_file:
    try:
        sheets = pd.read_excel(uploaded_file, sheet_name=None, engine="openpyxl")
        st.success("File uploaded and read successfully!")

        for sheet_name, df in sheets.items():
            st.subheader(f"📄 Sheet: {sheet_name}")
            st.dataframe(df)

        st.info("✅ Pro Forma, Cash Flow, Break-Even & Sensitivity calculations coming next...")

    except Exception as e:
        st.error(f"❌ Failed to read Excel file: {e}")
else:
    st.warning("Please upload an Excel file to continue.")
