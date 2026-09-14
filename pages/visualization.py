import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Cyber Attack Visualizations",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("cybersecurity_attacks.csv")

st.title("📊 Cyber Attack Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Attack Type Distribution")

    attack_counts = df["Attack Type"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(6, 5))

    ax1.pie(
        attack_counts.values,
        labels=attack_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax1.axis("equal")

    st.pyplot(fig1)

with col2:
    st.subheader("Protocol Distribution")

    protocol_counts = df["Protocol"].value_counts()

    fig2, ax2 = plt.subplots(figsize=(6, 5))

    ax2.bar(
        protocol_counts.index,
        protocol_counts.values
    )

    ax2.set_xlabel("Protocol")
    ax2.set_ylabel("Number of Records")

    st.pyplot(fig2)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("Packet Length Histogram")

    fig3, ax3 = plt.subplots(figsize=(6, 5))

    ax3.hist(
        df["Packet Length"],
        bins=30,
        edgecolor="black"
    )

    ax3.set_xlabel("Packet Length")
    ax3.set_ylabel("Frequency")

    st.pyplot(fig3)

with col4:
    st.subheader("Packet Length by Attack Type")

    fig4, ax4 = plt.subplots(figsize=(6, 5))

    sns.boxplot(
        data=df,
        x="Attack Type",
        y="Packet Length",
        ax=ax4
    )

    plt.xticks(rotation=45)

    st.pyplot(fig4)

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.subheader("Source Port vs Destination Port")

    sample_df = df.sample(min(2000, len(df)))

    fig5, ax5 = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=sample_df,
        x="Source Port",
        y="Destination Port",
        hue="Attack Type",
        ax=ax5
    )

    st.pyplot(fig5)

with col6:
    st.subheader("Average Anomaly Score by Severity")

    average_anomaly = df.groupby("Severity Level")["Anomaly Scores"].mean()

    fig6, ax6 = plt.subplots(figsize=(6, 5))

    ax6.bar(
        average_anomaly.index,
        average_anomaly.values
    )

    ax6.set_xlabel("Severity Level")
    ax6.set_ylabel("Average Anomaly Score")

    st.pyplot(fig6)

st.divider()

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig7, ax7 = plt.subplots(figsize=(14, 8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=ax7
)

st.pyplot(fig7)