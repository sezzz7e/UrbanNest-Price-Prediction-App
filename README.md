# 🏡 UrbanNest – House Price Prediction Application

UrbanNest is a Machine Learning-powered house price prediction application designed to help real estate professionals estimate residential property prices based on different property characteristics.

The application uses an optimized regression pipeline with trained preprocessing transformations to generate property price predictions through an interactive Streamlit web interface.

<p align="center">

  🚀 **Live Demo:** [UrbanNest Price Predictor](https://urbannest-price-predictor.streamlit.app/)

  💻 **GitHub Repository:** [UrbanNest – House Price Prediction](https://github.com/sezzz7e/UrbanNest-Price-Prediction-App)

</p>

---

## 📌 Project Overview

UrbanNest predicts residential property prices using important property features such as living area, lot size, bedrooms, bathrooms, overall quality, construction year, garage capacity, neighborhood, and house style.

This project covers the complete Machine Learning workflow, including:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and comparison
- Hyperparameter optimization
- Model evaluation
- Model serialization
- Web application development
- Cloud deployment

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Model development and training |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing and model evaluation |
| XGBoost | Regression model |
| Joblib | Model serialization |
| Streamlit | Interactive web application |
| GitHub | Version control and project hosting |
| Streamlit Community Cloud | Application deployment |

## 📊 Dataset

**Dataset:** Ames Housing Dataset

| Dataset Information | Details |
|---|---|
| Total Records | 2,930 |
| Target Variable | `SalePrice` |
| Problem Type | Regression |
| Data Type | Residential Housing Data |

The dataset contains information about residential properties, including their size, quality, construction details, location, and sale prices.

## ✨ Application Features

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
- Estimated property value displayed in USD

## 🏠 How to Use

1. Open the [UrbanNest Live Application](https://urbannest-price-predictor.streamlit.app/).
2. Enter the property's living area.
3. Enter the lot area.
4. Select the number of bedrooms and bathrooms.
5. Choose the overall property quality.
6. Enter the construction and remodeling years.
7. Select the garage capacity.
8. Choose the neighborhood and house style.
9. Click the **Predict House Price** button.
10. View the estimated property value in USD.

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

- Handled missing numerical values using median imputation.
- Handled missing categorical values using most-frequent imputation.
- Applied StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.
- Used a ColumnTransformer to manage numerical and categorical preprocessing.

### 2. Feature Engineering

Created additional property-related features to improve model performance:

- `House_Age`
- `Remodel_Age`
- `Total_Bathrooms`
- `Total_Porch_Area`
- `Total_Finished_Area`

### 3. Model Training and Comparison

- Trained and compared multiple regression models.
- Selected XGBoost Regression as the optimized model.
- Evaluated model performance using regression metrics.
- Used 5-fold cross-validation.

### 4. Hyperparameter Optimization

Applied `RandomizedSearchCV` to search for suitable XGBoost hyperparameters and improve prediction performance.

### 5. Model Serialization

The complete fitted regression pipeline was saved using Joblib.

The serialized pipeline includes:

- Numerical preprocessing
- Categorical preprocessing
- Trained XGBoost regression model

This allows the application to load the trained model and generate predictions without retraining it.

## 📈 Model Evaluation

The optimized regression model was evaluated using the following metrics:

| Evaluation Metric | Result |
|---|---|
| Mean Absolute Error (MAE) | Replace with actual result |
| Root Mean Squared Error (RMSE) | Replace with actual result |
| R² Score | Replace with actual result |

*Note: Update these values with the final evaluation results from Task 2.*

## 🚀 Local Installation

Follow these steps to run UrbanNest on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/sezzz7e/UrbanNest-Price-Prediction-App.git
```

### 2. Navigate to the Project Directory

```bash
cd UrbanNest-Price-Prediction-App
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

### 5. Open the Application

Visit the following local URL in your browser:

```text
http://localhost:8501
```

## ☁️ Deployment

The UrbanNest application is deployed using **Streamlit Community Cloud** and connected to the GitHub repository.

**Live Application:**

https://urbannest-price-predictor.streamlit.app/

**GitHub Repository:**

https://github.com/sezzz7e/UrbanNest-Price-Prediction-App

## ⚠️ Limitations

- The model is trained using historical Ames Housing Dataset records.
- Predictions may not represent current real estate market prices.
- Some property features may use default values derived from the training data.
- The model's predictions depend on the quality and characteristics of the training dataset.
- Predictions are estimates and should not be considered guaranteed property valuations.

## 🔮 Future Improvements

- Incorporate additional housing datasets.
- Improve prediction accuracy through further feature engineering.
- Add more property-related input features.
- Enhance the user interface and data visualizations.
- Explore additional regression algorithms.
- Improve model performance through further optimization.

## 👨‍💻 Author

**Abdullah Shehzad**

Software Engineering Student | Machine Learning Enthusiast

- **GitHub Profile:** [@sezzz7e](https://github.com/sezzz7e)
- **Project Repository:** [UrbanNest – House Price Prediction](https://github.com/sezzz7e/UrbanNest-Price-Prediction-App)
- **Live Application:** [UrbanNest Price Predictor](https://urbannest-price-predictor.streamlit.app/)

---

<p align="center">

  ⭐ If you find this project interesting, consider giving the repository a star!

  **Built with Python, Machine Learning, and Streamlit.**

</p>
