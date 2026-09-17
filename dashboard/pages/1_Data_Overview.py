import streamlit as st
import pandas as pd

# -------------------------------------------------------
# Page Title
# -------------------------------------------------------

st.title("📊 Data Overview")

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = pd.read_csv("data/processed/application_train_clean.csv")

# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", f"{df.shape[0]:,}")

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    memory = df.memory_usage(deep=True).sum() / (1024 ** 2)
    st.metric("Memory Usage", f"{memory:.1f} MB")

st.divider()

# -------------------------------------------------------
# Dataset Preview
# -------------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Data Types
# -------------------------------------------------------

st.subheader("Column Data Types")

types = (
    df.dtypes
      .astype(str)
      .value_counts()
      .rename_axis("Data Type")
      .reset_index(name="Count")
)

st.bar_chart(
    types.set_index("Data Type")
)

st.dataframe(
    types,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Missing Values
# -------------------------------------------------------

st.subheader("Missing Values")

missing = (
    df.isnull()
      .sum()
      .reset_index()
)

missing.columns = [
    "Column",
    "Missing Values"
]

missing = (
    missing[missing["Missing Values"] > 0]
    .sort_values(
        by="Missing Values",
        ascending=False
    )
)

if missing.empty:
    st.success("✅ No Missing Values Found")
else:
    st.dataframe(
        missing,
        use_container_width=True
    )

st.divider()

# -------------------------------------------------------
# Numerical Summary
# -------------------------------------------------------

st.subheader("Numerical Features Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Target Variable Distribution
# -------------------------------------------------------

st.subheader("Loan Repayment Distribution")

target_counts = df["TARGET"].value_counts().sort_index()

target_counts.index = [
    "No Default",
    "Default"
]

st.bar_chart(target_counts)