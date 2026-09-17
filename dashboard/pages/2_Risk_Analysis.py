import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Title
# -----------------------------
st.title("📈 Risk Analysis")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/processed/application_train_risk_scores.csv")

st.success("CSV Loaded Successfully!")

# -----------------------------
# Dataset Info
# -----------------------------
st.write(df.shape)

st.dataframe(df.head(), use_container_width=True)

# -----------------------------
# Loan Repayment Distribution
# -----------------------------
st.subheader("Loan Repayment Distribution")

default_counts = df["TARGET"].value_counts()

st.bar_chart(default_counts)

# -----------------------------
# Risk Score Statistics
# -----------------------------
st.subheader("Risk Score Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Risk Score",
    f"{df['RISK_SCORE'].mean():.2f}"
)

col2.metric(
    "Maximum Risk Score",
    f"{df['RISK_SCORE'].max():.2f}"
)

col3.metric(
    "Minimum Risk Score",
    f"{df['RISK_SCORE'].min():.2f}"
)

# -----------------------------
# Risk Categories
# -----------------------------
st.subheader("Customer Risk Categories")

risk_counts = df["RISK_CATEGORY"].value_counts()

risk_df = (
    risk_counts.rename_axis("Risk Category")
               .reset_index(name="Customers")
)

st.dataframe(risk_df, use_container_width=True)

# -----------------------------
# Histogram of Risk Scores
# -----------------------------
st.subheader("Distribution of Risk Scores")

fig, ax = plt.subplots(figsize=(8, 4))

ax.hist(
    df["RISK_SCORE"],
    bins=30,
    edgecolor="black"
)

ax.set_xlabel("Risk Score")
ax.set_ylabel("Number of Customers")
ax.set_title("Distribution of Risk Scores")

st.pyplot(fig)

plt.close(fig)