import streamlit as st
import pandas as pd

df = pd.read_csv("cybersecurity_attacks.csv")

st.title("🛡️ Cyber Attack Prediction System")

st.markdown("""
### Machine Learning Based Intrusion Detection

This project predicts cyber attacks using machine learning algorithms.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Total Features", len(df.columns))
col3.metric("Attack Types", df["Attack Type"].nunique())
col4.metric("Protocols", df["Protocol"].nunique())

st.subheader("Dataset Preview")
st.dataframe(df.head())