import streamlit as st
import pandas as pd

df = pd.read_csv("cybersecurity_attacks.csv")

st.title("📋 Dataset Analysis")

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("Column Information")
st.write(df.dtypes)

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Statistical Summary")
st.write(df.describe())