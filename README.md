# ML Regression Practice

Training linear and logistic regression with custom and HuggingFace datasets.

## Project Overview

This repository contains my practice implementations of:

- Linear regression (basic and with regularization)
- Logistic regression
- Experiments with custom datasets and HuggingFace datasets

## Setup

### Create Environment

```bash
conda create -n ml-regression python=3.10
conda activate ml-regression
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Jupyter Lab

```bash
jupyter lab
```

## Repository Structure

```
ml-regression-practice/
├── notebooks/
│   └── 01_linear_regression_basic.ipynb
├── data/
│   ├── 01_city_pop_restaurant_profit_training.txt
│   └── 02_city_pop_restaurant_profit_training.txt
├── utils.py
├── requirements.txt
└── README.md
```

## Usage

1. Navigate to the `notebooks/` folder in Jupyter Lab
2. Open the desired notebook
3. Run cells to see implementations and results

## Datasets

- Custom datasets: City population vs restaurant profit data
- Future: Will include experiments with HuggingFace datasets
