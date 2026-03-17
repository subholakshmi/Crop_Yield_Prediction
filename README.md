# Crop_Yield_Prediction
# Crop Yield Prediction using Machine Learning

This project predicts agricultural crop yield using environmental and agricultural factors such as rainfall, temperature, and pesticide usage.  
A machine learning model was trained using historical agricultural datasets and deployed using a Streamlit web application for real-time predictions.

---

## Project Overview

Crop yield prediction is important for improving agricultural planning and food security.  
This project uses machine learning techniques to analyze agricultural data and predict crop yield based on environmental conditions.

The system takes inputs such as:
- Year
- Rainfall
- Average Temperature
- Pesticides Usage
- Country
- Crop Type

and predicts the expected crop yield.

---

## Dataset

The project uses multiple agricultural datasets which were merged during preprocessing:

- Crop Yield Dataset
- Rainfall Dataset
- Temperature Dataset
- Pesticides Usage Dataset

These datasets were combined using **Year** and **Area (Country)** to create a final dataset for training.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

---

## Machine Learning Models

The following models were used for prediction:

- Linear Regression (Baseline Model)
- Random Forest Regressor (Final Model)

Random Forest was chosen as the final model due to better performance.

---

## Data Processing Pipeline

1. Data Collection
2. Data Cleaning
3. Dataset Merging
4. Feature Engineering
5. One-Hot Encoding for categorical variables
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Deployment with Streamlit

---

## Model Evaluation

Model performance was evaluated using:

- R² Score
- Root Mean Squared Error (RMSE)

Random Forest showed better prediction accuracy compared to Linear Regression.

---

## Project Structure

