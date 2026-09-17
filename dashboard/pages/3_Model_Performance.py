import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🤖 Model Performance")

st.write(
    "Comparison of the machine learning models developed for predicting loan default."
)

# ---------------------------------------------------------
# Model Comparison Metrics
# ---------------------------------------------------------

results = pd.DataFrame({
    "Model": ["Logistic Regression", "XGBoost"],
    "Accuracy": [0.9195, 0.7155],
    "Precision": [0.5546, 0.1714],
    "Recall": [0.0133, 0.6584],
    "F1 Score": [0.0260, 0.2720],
    "ROC-AUC": [0.7489, 0.7568]
})

st.subheader("📊 Model Comparison")

st.dataframe(results, use_container_width=True)

# ---------------------------------------------------------
# Best Model
# ---------------------------------------------------------

best_model = results.loc[results["ROC-AUC"].idxmax()]

st.success(
    f"🏆 Best Performing Model: **{best_model['Model']}** "
    f"(ROC-AUC = {best_model['ROC-AUC']:.4f})"
)

# ---------------------------------------------------------
# ROC-AUC Comparison Chart
# ---------------------------------------------------------

st.subheader("ROC-AUC Comparison")

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    results["Model"],
    results["ROC-AUC"]
)

ax.set_ylabel("ROC-AUC Score")
ax.set_ylim(0.70,0.80)

for i,v in enumerate(results["ROC-AUC"]):
    ax.text(i,v+0.001,f"{v:.4f}",ha="center")

st.pyplot(fig)

plt.close(fig)

# ---------------------------------------------------------
# Metric Comparison
# ---------------------------------------------------------

st.subheader("Evaluation Metrics Comparison")

metric = st.selectbox(
    "Choose Evaluation Metric",
    ["Accuracy","Precision","Recall","F1 Score","ROC-AUC"]
)

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    results["Model"],
    results[metric]
)

ax.set_ylabel(metric)

for i,v in enumerate(results[metric]):
    ax.text(i,v+0.01,f"{v:.3f}",ha="center")

st.pyplot(fig)

plt.close(fig)

# ---------------------------------------------------------
# Business Interpretation
# ---------------------------------------------------------

st.subheader("📌 Business Interpretation")

st.markdown("""
### Logistic Regression
- Very high overall accuracy.
- Very poor recall for loan defaulters.
- Misses most risky customers.

### XGBoost
- Better Recall.
- Better ROC-AUC.
- Better identifies customers likely to default.

### Conclusion
Although Logistic Regression has higher accuracy, the dataset is highly imbalanced.
For credit risk prediction, identifying risky customers is more important than maximizing accuracy.
Therefore, **XGBoost is selected as the final model** because it provides significantly better Recall and ROC-AUC.
""")