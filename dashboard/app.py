import importlib

# Load Streamlit dynamically so static analyzers do not report a missing
# import when the dependency is installed only in the dashboard environment.
st = importlib.import_module("streamlit")

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Credit Risk Analytics Dashboard",
    page_icon="🏦",
    layout="wide"
)

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🏦 Credit Risk Analytics Dashboard")

st.markdown(
"""
### Machine Learning-Based Loan Default Prediction

An interactive dashboard developed using **Machine Learning**
to predict customer loan default risk using the
**Home Credit Default Risk Dataset**.
"""
)

st.divider()

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    "307,511"
)

col2.metric(
    "Features",
    "221"
)

col3.metric(
    "Best Model",
    "XGBoost"
)

col4.metric(
    "ROC-AUC",
    "0.7568"
)

st.divider()

# -------------------------------------------------------
# Dataset Information
# -------------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📊 Dataset Summary")

    st.markdown("""
- **Dataset:** Home Credit Default Risk
- **Records:** 307,511 Customers
- **Features:** 221
- **Target:** Loan Default Prediction
- **Missing Values:** Handled
- **Feature Engineering:** Completed
""")

with right:

    st.subheader("🛠 Technology Stack")

    st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Streamlit
""")

st.divider()

# -------------------------------------------------------
# Project Workflow
# -------------------------------------------------------

st.subheader("📈 Machine Learning Pipeline")

st.code("""
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Business Insights
      │
      ▼
Interactive Dashboard
""")

st.divider()

# -------------------------------------------------------
# Project Objective
# -------------------------------------------------------

st.subheader("🎯 Project Objective")

st.info(
"""
This project predicts the probability of customer loan default
using Machine Learning models.

The dashboard helps financial institutions identify
high-risk applicants, improve loan approval decisions,
and reduce financial losses.
"""
)

st.divider()

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.caption(
"Developed by **Nitish Kumar** | Credit Risk Analytics Dashboard"
)