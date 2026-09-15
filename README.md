# Cybersecurity Attack Analysis and Detection System

A machine learning project developed during my internship to analyze cybersecurity attack data and detect different types of cyber threats.

The project uses data preprocessing, feature engineering, visualization, and a tree-based machine learning model called **Random Forest Classifier**.

## Machine Learning Model

The main model used in this project is:

**Random Forest Classifier**

Random Forest is a tree-based machine learning algorithm that creates multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.

In this project, the Random Forest model is used to classify cybersecurity records into different attack types based on network and traffic-related features.

## Model Workflow

```text
Cybersecurity Dataset
        ↓
Data Cleaning
        ↓
Feature Selection
        ↓
Categorical Encoding
        ↓
Train-Test Split
        ↓
Random Forest Classifier
        ↓
Multiple Decision Trees
        ↓
Combined Prediction
        ↓
Cyber Attack Classification
        ↓
Streamlit Dashboard