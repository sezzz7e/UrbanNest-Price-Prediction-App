
# UrbanNest - House Price Prediction Application 🏡

UrbanNest is a Machine Learning-powered house price prediction application designed to help real estate professionals estimate residential property prices based on different property characteristics.

The application uses an optimized regression pipeline with trained preprocessing transformations to generate property price predictions through an interactive Streamlit web interface.

🚀 **Live Demo:** https://urbannest-price-predictor.streamlit.app/

💻 **GitHub Repository:** https://github.com/sezzz7e/urbannest-price-prediction-app

---

## Project Overview

UrbanNest predicts residential property prices using important property features such as living area, lot size, bedrooms, bathrooms, overall quality, construction year, garage capacity, neighborhood, and house style.

The project covers the complete Machine Learning workflow, including data preprocessing, feature engineering, model training, hyperparameter optimization, model evaluation, serialization, and deployment.

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- GitHub

## Dataset

- **Dataset:** Ames Housing Dataset
- **Total Records:** 2,930
- **Target Variable:** SalePrice
- **Problem Type:** Regression

## Application Features

- Interactive property input form
- Living area and lot area
- Bedrooms and bathrooms
- Overall property quality
- Construction and remodeling years
- Garage capacity
- Neighborhood selection
- House style selection
- Instant house price prediction
- Input validation and error handling
- User-friendly Streamlit interface

## How to Use

1. Open the UrbanNest live application.
2. Enter the property's living area.
3. Enter the lot area.
4. Select the number of bedrooms and bathrooms.
5. Choose the overall property quality.
6. Enter construction and remodeling years.
7. Select garage capacity.
8. Choose the neighborhood and house style.
9. Click the **Predict House Price** button.
10. View the estimated property value in USD.

## Machine Learning Workflow

### 1. Data Preprocessing

- Handled missing numerical values using median imputation.
- Handled missing categorical values using most-frequent imputation.
- Applied StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.

### 2. Feature Engineering

Created additional property-related features:

- House_Age
- Remodel_Age
- Total_Bathrooms
- Total_Porch_Area
- Total_Finished_Area

### 3. Model Training and Optimization

- Compared multiple regression models.
- Selected XGBoost Regression as the optimized model.
- Applied RandomizedSearchCV for hyperparameter optimization.
- Used 5-fold cross-validation for model evaluation.

### 4. Model Serialization

The complete fitted regression pipeline was saved using Joblib, preserving the trained preprocessing and prediction components.

## Model Evaluation

The optimized model was evaluated using the following regression metrics:

| Evaluation Metric | Result |
|---|---|
| MAE | Add your actual Task 2 result |
| RMSE | Add your actual Task 2 result |
| R² Score | Add your actual Task 2 result |

## Local Installation

**1. Clone the repository**

```bash
git clone https://github.com/sezzz7e/urbannest-price-prediction-app.git
```

**2. Navigate into the project folder**

```bash
cd urbannest-price-prediction-app
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run app.py
```

**5. Open in your browser**

```text
http://localhost:8501
```

## Live Deployment

The application is deployed using Streamlit Community Cloud and connected to GitHub.

**Live Application:** https://urbannest-price-predictor.streamlit.app/

## Limitations

- The model is trained using historical Ames Housing Dataset records.
- Predictions may not represent current real estate market prices.
- Some property features may use default values derived from the training data.
- Predictions are estimates and should not be considered guaranteed property valuations.

## Author

**Abdullah Shehzad**

Software Engineering Student | Machine Learning Enthusiast

- **GitHub:** https://github.com/sezzz7e
- **Project Repository:** https://github.com/sezzz7e/urbannest-price-prediction-app
- **Live Application:** https://urbannest-price-predictor.streamlit.app/

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Machine Learning, and Streamlit.**Student
Machine Learning Internship Project
