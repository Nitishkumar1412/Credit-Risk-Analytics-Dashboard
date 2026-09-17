import streamlit as st
import pandas as pd
import joblib

st.title("🔮 Customer Risk Prediction")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/xgboost_credit_risk_model.pkl")

model = load_model()

# -----------------------------
# Load Datasets
# -----------------------------
@st.cache_data
def load_data():
    customer_df = pd.read_csv(
        "data/processed/application_train_clean.csv"
    )

    feature_df = pd.read_csv(
        "data/processed/model_features.csv"
    )

    return customer_df, feature_df

customer_df, feature_df = load_data()

# -----------------------------
# Customer Selection
# -----------------------------
st.subheader("Select Customer")

customer_ids = customer_df["SK_ID_CURR"].tolist()

customer_id = st.selectbox(
    "Customer ID",
    customer_ids
)

# Get row index
idx = customer_df.index[
    customer_df["SK_ID_CURR"] == customer_id
][0]

# -----------------------------
# Customer Details
# -----------------------------
customer = customer_df.loc[idx]

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Income", f"₹{customer['AMT_INCOME_TOTAL']:,.0f}")
    st.metric("Credit Amount", f"₹{customer['AMT_CREDIT']:,.0f}")
    st.metric("Age (Years)", int(abs(customer["DAYS_BIRTH"]) / 365))

with col2:
    st.metric("Employment Years", round(customer["YEARS_EMPLOYED"], 1))
    st.metric("Children", int(customer["CNT_CHILDREN"]))
    st.metric("Family Members", customer["CNT_FAM_MEMBERS"])

st.divider()

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Risk"):

    X = feature_df.iloc[[idx]]

    probability = model.predict_proba(X)[0][1]

    if probability < 0.30:
        category = "🟢 Low Risk"
        recommendation = "✅ Approve Loan"

    elif probability < 0.60:
        category = "🟡 Medium Risk"
        recommendation = "⚠ Manual Review Required"

    else:
        category = "🔴 High Risk"
        recommendation = "❌ Reject Loan"

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Default Probability",
            f"{probability*100:.2f}%"
        )

        st.metric(
            "Risk Score",
            f"{probability:.3f}"
        )

    with col2:
        st.success(category)

        st.info(recommendation)

    st.progress(float(probability))