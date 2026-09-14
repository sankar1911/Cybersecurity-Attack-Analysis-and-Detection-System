import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("cybersecurity_attacks.csv")

model = joblib.load("random_forest_model.pkl")

st.title("🎯 Cyber Attack Prediction")

st.info("Enter network traffic information below.")

col1, col2 = st.columns(2)

with col1:
    source_port = st.number_input(
        "Source Port",
        min_value=0,
        max_value=65535,
        value=80
    )

    destination_port = st.number_input(
        "Destination Port",
        min_value=0,
        max_value=65535,
        value=443
    )

    protocol = st.selectbox(
        "Protocol",
        df["Protocol"].dropna().unique()
    )

    traffic_type = st.selectbox(
        "Traffic Type",
        df["Traffic Type"].dropna().unique()
    )

with col2:
    packet_length = st.number_input(
        "Packet Length",
        min_value=0,
        value=500
    )

    anomaly_score = st.slider(
        "Anomaly Score",
        min_value=0.0,
        max_value=1.0,
        value=0.5
    )

    severity = st.selectbox(
        "Severity Level",
        df["Severity Level"].dropna().unique()
    )

if st.button("Predict Attack"):

    sample = pd.DataFrame({
        "Source Port": [source_port],
        "Destination Port": [destination_port],
        "Protocol": [protocol],
        "Packet Length": [packet_length],
        "Traffic Type": [traffic_type],
        "Anomaly Scores": [anomaly_score],
        "Severity Level": [severity]
    })

    prediction = model.predict(sample)

    st.success(f"Predicted Attack Type: {prediction[0]}")