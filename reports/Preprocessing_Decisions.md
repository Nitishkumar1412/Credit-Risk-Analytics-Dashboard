# Preprocessing Decisions

## Decision 1: High Missing Value Columns

### Decision

Columns with more than 60% missing values were reviewed individually.

### Columns Dropped

- COMMONAREA_MEDI
- COMMONAREA_AVG
- COMMONAREA_MODE
- NONLIVINGAPARTMENTS_MODE
- NONLIVINGAPARTMENTS_AVG
- NONLIVINGAPARTMENTS_MEDI
- FONDKAPREMONT_MODE
- LIVINGAPARTMENTS_MODE
- LIVINGAPARTMENTS_AVG
- LIVINGAPARTMENTS_MEDI
- FLOORSMIN_AVG
- FLOORSMIN_MODE
- FLOORSMIN_MEDI
- YEARS_BUILD_MEDI
- YEARS_BUILD_MODE
- YEARS_BUILD_AVG

### Column Retained

- OWN_CAR_AGE

### Reason

The dropped columns contained more than 60% missing values and were not considered essential for the initial credit risk model. `OWN_CAR_AGE` was retained because missing values indicate applicants without a car, which is meaningful information rather than an error.

## Decision 2: Handling Placeholder Values

### Column

- DAYS_EMPLOYED

### Issue

The value `365243` was identified as a placeholder representing unknown employment duration rather than a valid number of employment days.

### Action Taken

- Replaced `365243` with `NaN`
- Imputed missing values using the median
- Recalculated the `YEARS_EMPLOYED` feature

### Reason

Keeping the placeholder would create unrealistic employment durations (approximately 1000 years), which would negatively affect statistical analysis and predictive modeling.