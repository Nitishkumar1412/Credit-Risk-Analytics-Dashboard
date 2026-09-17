# Data Quality Report

## Dataset Name

Home Credit Default Risk

---

## Dataset Dimensions

- Rows: **307,511**
- Columns: **122**

---

## Data Types

| Type | Count |
|------|------:|
| Float | 65 |
| Integer | 41 |
| Categorical (String) | 16 |

---

## Target Variable Distribution

| Class | Percentage |
|-------|-----------:|
| No Default (0) | 91.93% |
| Default (1) | 8.07% |

---

## Missing Values

Several columns contain a high percentage of missing values.

Top missing columns:

| Column | Missing % |
|--------|----------:|
| COMMONAREA_MEDI | 69.87% |
| COMMONAREA_AVG | 69.87% |
| COMMONAREA_MODE | 69.87% |
| NONLIVINGAPARTMENTS_MEDI | 69.43% |
| NONLIVINGAPARTMENTS_MODE | 69.43% |

These columns will be evaluated during the preprocessing phase to determine whether they should be imputed or removed.

---

## Overall Assessment

- Large real-world banking dataset.
- Significant missing values present.
- No major structural issues identified.
- Dataset is suitable for exploratory data analysis and predictive modeling after preprocessing.