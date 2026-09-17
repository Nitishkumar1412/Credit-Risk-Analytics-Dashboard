# Data Preprocessing Report

## Objective

Prepare the Home Credit loan application dataset for exploratory data analysis and predictive modeling by addressing data quality issues and engineering meaningful business features.

---

## Dataset Overview

- Original Rows: 307,511
- Original Columns: 122

---

## Preprocessing Steps

### 1. Removed Highly Sparse Columns

- Reviewed columns with more than 60% missing values.
- Removed 16 columns that were not considered essential for the initial credit risk analysis.
- Retained `OWN_CAR_AGE` because missing values indicate applicants without a car.

---

### 2. Missing Value Treatment

- Numerical features were imputed using the median.
- Categorical features were filled with "Unknown".
- `OWN_CAR_AGE` was intentionally left unchanged.

---

### 3. Placeholder Value Handling

The `DAYS_EMPLOYED` column contained a placeholder value (`365243`) representing unknown employment duration.

Actions taken:

- Replaced placeholder with NaN
- Filled using median
- Recreated `YEARS_EMPLOYED`

---

### 4. Feature Engineering

Created six new business features:

- AGE_YEARS
- YEARS_EMPLOYED
- CREDIT_INCOME_RATIO
- ANNUITY_INCOME_RATIO
- HAS_CAR
- HAS_REALTY

---

### 5. Data Validation

- Duplicate Records: 0
- Final Dataset Columns: 112

---

## Output

Processed dataset saved to:

data/processed/application_train_clean.csv