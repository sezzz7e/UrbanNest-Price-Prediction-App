
# UrbanNest - House Price Prediction Application

## Project Overview

UrbanNest is a machine learning powered house price
prediction application designed to help real estate
agents estimate residential property prices.

The application uses a trained regression pipeline
and preprocessing transformations to generate
property price predictions.

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- GitHub

## Dataset

Ames Housing Dataset

Total Records: 2,930

Target Variable: SalePrice

Problem Type: Regression

## Features

- Interactive property input form
- Living area and lot area
- Bedrooms and bathrooms
- Overall quality
- Construction and remodeling years
- Garage capacity
- Neighborhood and house style
- Real-time price estimation
- Input validation and error handling

## How to Use

1. Open the live application.
2. Enter the living area.
3. Enter lot area.
4. Select bedrooms and bathrooms.
5. Choose overall property quality.
6. Enter construction and remodeling years.
7. Select garage capacity.
8. Select neighborhood and house style.
9. Click Predict House Price.
10. View the estimated property value in USD.

## Local Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/UrbanNest-Price-Prediction-App.git

Navigate into the folder:

cd UrbanNest-Price-Prediction-App

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Model Information

The application uses the best regression pipeline
selected during Task 2.

The complete fitted pipeline is saved using Joblib.

It includes the trained preprocessing and prediction
components used by the model.

## Model Evaluation

MAE: [Insert actual Task 2 MAE]

RMSE: [Insert actual Task 2 RMSE]

R2 Score: [Insert actual Task 2 R2]

## Live Demo

[Open UrbanNest Live Application](YOUR_STREAMLIT_URL)

## Limitations

- The model uses historical Ames housing data.
- Predictions may not represent current real estate prices.
- Some features use training-data defaults.
- Predictions are estimates, not guaranteed valuations.

## Author

Abdullah Shehzad

Software Engineering Student
Machine Learning Internship Project
