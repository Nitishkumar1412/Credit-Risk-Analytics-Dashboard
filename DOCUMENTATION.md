# Credit Risk Analytics & Portfolio Optimization

## Project Documentation

---

# Table of Contents

1. Project Overview
2. Problem Statement
3. Business Objective
4. Dataset Description
5. Project Architecture
6. Data Preprocessing
7. Exploratory Data Analysis
8. Feature Engineering
9. Predictive Modeling
10. Model Evaluation
11. Business Insights
12. Dashboard Overview
13. Project Structure
14. Challenges Faced
15. Limitations
16. Future Enhancements
17. Conclusion

---

# 1. Project Overview

Credit Risk Analytics & Portfolio Optimization is an end-to-end Machine Learning project that predicts the probability of loan default using customer demographic, financial, and historical loan information.

The project demonstrates a complete data science workflow starting from raw data preprocessing, exploratory data analysis, feature engineering, predictive modeling, business insight generation, and finally deployment through an interactive Streamlit dashboard.

The objective is to help financial institutions identify high-risk customers before approving loans, thereby reducing default rates and improving portfolio quality.

---

# 2. Problem Statement

Financial institutions process thousands of loan applications every day. Approving loans without accurately assessing customer risk can lead to significant financial losses.

Traditional rule-based credit scoring systems often fail to capture complex relationships between customer characteristics and repayment behavior.

The goal of this project is to build a machine learning model capable of estimating the probability that a customer will default on a loan.

---

# 3. Business Objective

The project aims to support better lending decisions by:

- Identifying high-risk applicants
- Reducing loan defaults
- Improving portfolio profitability
- Supporting risk-based pricing strategies
- Providing explainable analytics through interactive dashboards

---

# 4. Dataset Description

Dataset Name:
Home Credit Default Risk

Source:
Kaggle

Dataset Size

- Customers: 307,511
- Features: 221 (raw)
- Final Features Used: 112
- Target Variable:
    TARGET
    0 → Loan Repaid
    1 → Loan Default

The dataset contains:

- Customer demographics
- Employment information
- Credit history
- Income details
- Family information
- Housing details
- Previous loan records

---

# 5. Project Architecture

Raw Dataset

↓

Data Cleaning

↓

Missing Value Handling

↓

Feature Engineering

↓

Exploratory Data Analysis

↓

Model Training

↓

Model Evaluation

↓

Business Insights

↓

Streamlit Dashboard

---

# 6. Data Preprocessing

The preprocessing stage included:

• Removing unnecessary columns

• Handling missing values

• Treating inconsistent records

• Encoding categorical variables

• Scaling numerical features where required

• Creating additional business-driven features

The final cleaned dataset was used for model development.

---

# 7. Exploratory Data Analysis

Several analyses were performed including:

Income Distribution

Credit Amount Distribution

Age Analysis

Employment Analysis

Loan Repayment Distribution

Missing Value Analysis

Correlation Analysis

Occupation Risk Analysis

Education Level Analysis

Customer Segmentation

EDA helped identify important patterns that influenced loan default.

---

# 8. Feature Engineering

Important engineered features include:

- Credit to Income Ratio

- Age Groups

- Income Groups

- Credit Groups

- Employment Years

- Customer Risk Categories

Feature engineering significantly improved model performance.

---

# 9. Predictive Modeling

Two machine learning algorithms were developed and evaluated.

## Logistic Regression

Advantages

- Simple
- Fast
- Interpretable

Limitations

- Very low Recall
- Misses many risky customers

---

## XGBoost

Advantages

- Better Recall
- Better ROC-AUC
- Handles non-linear relationships
- Better overall business performance

XGBoost was selected as the final production model.

---

# 10. Model Evaluation

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|--------|----------|-----------|---------|----------|----------|
| Logistic Regression | 0.9195 | 0.5546 | 0.0133 | 0.0260 | 0.7489 |
| XGBoost | 0.7155 | 0.1714 | 0.6584 | 0.2720 | **0.7568** |

Although Logistic Regression achieved higher accuracy, it failed to identify most defaulting customers due to severe class imbalance.

XGBoost demonstrated significantly higher Recall and better ROC-AUC, making it more suitable for credit risk prediction.

---

# 11. Business Insights

The analysis revealed several important business findings.

- Younger applicants showed relatively higher default rates.

- Lower income groups were associated with increased credit risk.

- Certain occupation categories exhibited elevated default probabilities.

- Higher education levels generally corresponded to lower default rates.

- Income-to-credit ratio proved to be an important predictor.

These insights can support lending strategy and customer segmentation.

---

# 12. Dashboard Overview

The Streamlit dashboard provides:

- Dataset Overview
- Risk Analysis
- Model Performance Comparison
- Customer Risk Prediction
- Business Insights
- Interactive Visualizations

The dashboard enables users to explore customer risk without writing any code.

---

# 13. Project Structure

```
Credit-Risk-Analytics/

dashboard/
images/
models/
notebooks/
reports/
requirements.txt
README.md
DOCUMENTATION.md
```

---

# 14. Challenges Faced

Major challenges encountered during development included:

- Large number of missing values

- High class imbalance

- High-dimensional dataset

- Feature selection

- Model comparison

- Dashboard integration

---

# 15. Limitations

Current limitations include:

- Dataset represents historical loan applications only.

- External economic indicators were not incorporated.

- Model explanations (e.g., SHAP values) are not included.

- Hyperparameter optimization was limited.

- The dashboard currently runs locally and is not deployed.

---

# 16. Future Enhancements

Potential improvements include:

- Streamlit Cloud deployment

- SHAP explainability

- Hyperparameter tuning

- Real-time prediction API

- Model monitoring

- Automated retraining pipeline

- Integration with SQL databases

- Power BI reporting

---

# 17. Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow for credit risk assessment.

Starting from raw customer data, the project applies preprocessing, exploratory analysis, feature engineering, predictive modeling, and interactive visualization to generate actionable business insights.

The final XGBoost model provides a strong balance between predictive performance and business usefulness, making it suitable for supporting credit approval decisions in financial institutions.

The project highlights practical applications of data analytics and machine learning in the banking and financial services domain.