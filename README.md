# Green Computing Project

This project compares binary classification pipelines on electronic health record (EHR) datasets using Python and R.

## Project Objectives

- Perform binary classification on 5 healthcare datasets
- Measure model performance using MCC(Matthews Correlation Coefficient)
- Measure execution time
- Measure energy consumption and CO2-equivalent emissions
- Compare a baseline and optimized implementation
- Reproduce the optimized pipeline in R

## Files

- `baseline.py` - Baseline Random Forest implementation
- `optimized.py` - Optimized Logistic Regression implementation
- `optimized_r.R` - R implementation of the optimized pipeline
- `compare_results.py` - Compares baseline and optimized results
- `baseline_results.csv` - Results from baseline model
- `optimized_results_final.csv` - Results from optimized model
- `comparison_results.csv` - Combined comparison table

## Requirements

Install required Python libraries

```bash 
pip install pandas numpy scikit-learn codecarbon
```

Install required R package:

```
install.packages("caret")
```

## Dataset

Place all CSV datasets inside the `data` folder.

The target variable must be the last column in each dataset. 

## Running the Scripts

Run baseline model:

```bash
python3 baseline.py
```

Run optimized model:

```bash
python3 optimized.py
```

Run result comparison:

```bash
python3 compare_results.py
```

Run R implementation:

```bash
Rscript optimized_r.R
```

## Measurements

### Python
- MCC
- Runtime
- Energy consumption
- CO2-equivalent emissions
- Measured using CodeCarbon

### R
- Accuracy
- Runtime
- Estimated energy consumption
- Estimated CO2-equivalent emissions

Energy and CO2 values in R were estimated using execution time and average device power consumption.

## Author

Rishpa Shrestha
