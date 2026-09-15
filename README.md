# Cyber Attack Detection Project

This project was developed during my internship to analyze cybersecurity attack data and identify different types of cyber attacks using Machine Learning.

The project uses data preprocessing, feature encoding, Random Forest classification, and Streamlit for displaying cybersecurity data and predictions.

## Project Features

- Loads and analyzes cybersecurity attack data
- Performs data preprocessing and feature selection
- Converts categorical data using OneHotEncoder
- Trains a Random Forest Classifier
- Saves the trained machine learning model
- Visualizes cybersecurity data using Matplotlib and Seaborn
- Provides an interactive Streamlit web application

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Joblib
- Streamlit
- Matplotlib
- Seaborn

## Project Structure

```text
CyberAttackProject/
│
├── pages/
│
├── app.py
├── train_model.py
├── cybersecurity_attacks.csv
├── requirements.txt
├── random_forest_model.pkl
└── README.md

## Model File

The trained Random Forest model is not included in the repository
because of GitHub's file size limit.

Run the following command to generate the model:

```bash
python train_model.py