## End to End Machine Learning Project
# Diamond Price Prediction 💎
## Overview

This project aims to predict the price of diamonds based on various features such as carat weight, cut, color, clarity, and depth percentage. Leveraging machine learning techniques, we have developed a model that can provide accurate predictions, allowing users to estimate diamond prices with confidence.

## Sample Images
![Image](https://github.com/RRaghulRajkumar/Diamond-price-Prediction/blob/main/demo/image1.png)

![Image](https://github.com/RRaghulRajkumar/Diamond-price-Prediction/blob/main/demo/image2.png)

## Demo Video

![Demo](https://github.com/RRaghulRajkumar/Diamond-price-Prediction/blob/main/demo/Diamond-price-demo.mp4?raw=true "Demo")

## Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Model](#model)

## Dataset

The dataset used for this project is sourced from [dataset source]. It includes information on diamond characteristics such as carat weight, cut, color, clarity, depth percentage, table percentage, and price.

## Features

- **Carat Weight:** The weight of the diamond in carats.
- **Cut:** The quality of the cut (Fair, Good, Very Good, Premium, Ideal).
- **Color:** The color grade of the diamond (from J to D, with J being the lowest and D being the highest).
- **Clarity:** The clarity grade of the diamond (from I1 to IF, with I1 being the lowest and IF being the highest).
- **Depth Percentage:** The total depth percentage (measured vertically from the culet to the table, divided by the average girdle diameter).
- **Table Percentage:** The width of the diamond's table expressed as a percentage of its average diameter.

## Model

We utilized a machine learning model, specifically [insert model type], to predict diamond prices. The model was trained on a labeled dataset, and its performance was evaluated based on metrics such as Mean Absolute Error (MAE) and R-squared.


## Introduction About the Data 📊

The dataset aims to predict the price of diamonds through Regression Analysis. It includes 10 independent variables:

1. **id:** Unique identifier of each diamond
2. **carat:** Carat (ct.) - unit of weight for gemstones and diamonds
3. **cut:** Quality of Diamond Cut
4. **color:** Color of Diamond
5. **clarity:** Diamond clarity - measure of purity and rarity
6. **depth:** Depth of diamond (in millimeters)
7. **table:** A diamond's table - facet seen when viewed face up
8. **x:** Diamond X dimension
9. **y:** Diamond Y dimension
10. **z:** Diamond Z dimension

**Target variable:**
- **price:** Price of the given Diamond.

[Dataset Source Link](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

## Purpose of Pipeline 🚀

In machine learning projects, a pipeline is crucial for streamlining and automating the workflow. In this project, the pipeline connects three essential steps:

1. **Simple Imputer:** Handles missing values in the dataset.
2. **Standard Scaler:** Scales numerical features to prevent domination of higher values during regression.
3. **Ordinal Encoding:** Converts categorical features with ranks into a numerical format.

By combining these steps into a pipeline, the data processing becomes more efficient and easier to replicate.

## Exploratory Data Analysis (EDA) 📈

Exploratory Data Analysis is a crucial phase in understanding the dataset's characteristics. It involves statistical and visual methods to uncover patterns, relationships, and potential outliers. EDA helps in making informed decisions about data preprocessing and feature selection.

## Feature Engineering 🔧

Feature engineering involves transforming raw data into a format suitable for machine learning models. In this project, ordinal encoding is employed for categorical features with ranks. This enhances the model's ability to capture meaningful relationships in the data.

## Machine Learning Algorithms 🤖

### Linear Regression 📏
Linear regression is a fundamental algorithm for predicting a continuous variable (in this case, the diamond price) based on the relationship with independent variables.

### Lasso 🔍
Lasso (Least Absolute Shrinkage and Selection Operator) is a regression technique that introduces a penalty term to the linear regression, encouraging sparsity in the model coefficients.

### Ridge 🚐
Ridge regression is another regularization technique that prevents overfitting by adding a penalty term to the linear regression, encouraging smaller coefficients.

### ElasticNet 🕸️
ElasticNet combines both L1 and L2 regularization, providing a balance between feature selection (Lasso) and coefficient shrinkage (Ridge).

## Model Training Performance 📊

### Linear Regression 📏
**RMSE:** 1014.63
**MAE:** 675.08
**R2_SQUARE:** 93.63%

### Lasso 🔍
**RMSE:** 1014.66
**MAE:** 676.24
**R2_SQUARE:** 93.63%

### Ridge 🚐
**RMSE:** 1014.63
**MAE:** 675.11
**R2_SQUARE:** 93.63%

### ElasticNet 🕸️
**RMSE:** 1533.35
**MAE:** 1060.94
**R2_SQUARE:** 85.45%


