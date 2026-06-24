# 🚗 Car Price Prediction App

This project is a Machine Learning-powered web application that predicts the selling price of a used car.

## Features
- Predicts car resale value
- Interactive web interface using Streamlit
- Built with Linear Regression
- User-friendly input fields
- Real-time predictions

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

## Input Features
- Manufacturing Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Number of Previous Owners

## Machine Learning Workflow
- Data Collection
- Data Cleaning and Preprocessing
- Feature Selection
- Train-Test Split
- Model Training using Linear Regression
- Model Evaluation
- Model Serialization using Pickle
- Streamlit Application Development
- Cloud Deployment

## Model Performance
Metric	Score
Training R² Score	~0.88
Testing R² Score	~0.84




## Output
- Estimated Selling Price of the Car

## Future Improvements
- Add car brand and model information
- Implement XGBoost and Random Forest models
- Improve UI/UX
- Deploy with custom domain


- ## 📊 Project Architecture

```text
Dataset
   │
   ▼
Data Cleaning & Preprocessing
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Linear Regression Model
   │
   ▼
Model Evaluation (R² Score)
   │
   ▼
Model Serialization (.pkl)
   │
   ▼
Streamlit Web Application
   │
   ▼
User Input
   │
   ▼
Predicted Car Price
