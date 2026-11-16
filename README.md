# 🏡 UrbanNest – House Price Prediction Application

## Project Overview

UrbanNest is a Machine Learning-powered house price prediction application developed to estimate residential property prices using property characteristics.

The application uses an optimized XGBoost regression pipeline with trained preprocessing transformations. Users can enter property details through an interactive Streamlit interface and receive an estimated house price.

**Live Application:** https://urbannest-price-predictor.streamlit.app/

**GitHub Repository:** https://github.com/sezzz7e/UrbanNest-Price-Prediction-App

---

## Technologies Used

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

---

## Dataset

**Dataset:** Ames Housing Dataset

| Dataset Information | Details |
|---|---|
| Total Records | 2,930 |
| Target Variable | `SalePrice` |
| Problem Type | Regression |
| Data Type | Residential Housing Data |

The dataset contains residential property information, including living area, lot size, construction details, property quality, neighborhood, and historical sale prices.

---

## Application Features

- Interactive property input form
- Living area and lot area input
- Bedroom selection
- Full and half bathroom selection
- Basement area input
- Overall property quality selection
- Construction and remodeling year inputs
- Garage capacity selection
- Neighborhood selection
- House style selection
- Input validation and error handling
- Instant house price prediction
- Estimated property value displayed in USD
- Expandable property details section

---

## How to Use

1. Open the [UrbanNest Live Application](https://urbannest-price-predictor.streamlit.app/).
2. Enter the property's living area.
3. Enter the lot area.
4. Select the number of bedrooms.
5. Enter the full and half bathroom counts.
6. Enter the basement area.
7. Select the overall property quality.
8. Enter the construction and remodeling years.
9. Select the garage capacity.
10. Choose the neighborhood and house style.
11. Click **Predict House Price**.
12. View the estimated property value.

The application displays the predicted price along with a property details section.

---

## Machine Learning Workflow

### 1. Data Preprocessing

The training workflow includes:

- Handling missing numerical values using median imputation.
- Handling missing categorical values using most-frequent imputation.
- Applying numerical scaling.
- Encoding categorical variables using OneHotEncoder.
- Combining preprocessing operations using ColumnTransformer.

### 2. Feature Engineering

Additional property-related features were created to improve the model's ability to learn property characteristics:

- `House_Age`
- `Remodel_Age`
- `Total_Bathrooms`
- `Total_Porch_Area`
- `Total_Finished_Area`

The same feature engineering transformations are applied to incoming property data before generating predictions.

### 3. Model Training and Comparison

- Multiple regression models were trained and compared.
- XGBoost Regression was selected as the optimized model.
- Model performance was evaluated using regression metrics.
- Five-fold cross-validation was used during model evaluation.

### 4. Hyperparameter Optimization

`RandomizedSearchCV` was used to explore XGBoost hyperparameter combinations and identify a suitable model configuration.

### 5. Model Serialization

The complete fitted regression pipeline was saved using Joblib.

The saved pipeline includes:

- Numerical preprocessing transformations.
- Categorical preprocessing transformations.
- The trained XGBoost regression estimator.

This allows the deployed application to load the trained model and generate predictions without retraining it.

---

## Model Evaluation

The model was evaluated using standard regression evaluation metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The final evaluation results were generated during the model development and optimization stage in Google Colab.

---

## Project Structure

```text
UrbanNest-Price-Prediction-App/
│
├── app.py
├── urbannest_best_model.joblib
├── model_metadata.json
├── requirements.txt
├── README.md
├── HANDOVER.md
└── .gitignore
```

### Important Files

| File | Description |
|---|---|
| `app.py` | Streamlit application and prediction logic |
| `urbannest_best_model.joblib` | Saved trained regression pipeline |
| `model_metadata.json` | Model feature information, input defaults, and selection options |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `HANDOVER.md` | Project handover information |
| `.gitignore` | Files excluded from Git tracking |

---

## Application Implementation

The live application is implemented in `app.py`.

The application uses the following process:

1. Loads the trained regression pipeline using Joblib.
2. Loads model metadata from `model_metadata.json`.
3. Collects property information through Streamlit input controls.
4. Uses metadata-provided default values for other required training features that are not directly exposed in the form.
5. Applies the same feature engineering transformations used during model development.
6. Passes the prepared input to the trained pipeline.
7. Displays the predicted property price.

The model and metadata are loaded using paths relative to the application script. This makes the application independent of a specific local working directory.

---

## Local Installation

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

Open the following address in your browser:

```text
http://localhost:8501
```

---

## Deployment

UrbanNest is deployed using **Streamlit Community Cloud** and connected to its public GitHub repository.

**Live Application:**

https://urbannest-price-predictor.streamlit.app/

**GitHub Repository:**

https://github.com/sezzz7e/UrbanNest-Price-Prediction-App

The deployment allows users and reviewers to access the prediction interface through a web browser without installing the project locally.

---

## Limitations

- The model is trained using historical Ames Housing Dataset records.
- Predictions may not represent current real estate market prices.
- Some required model features are populated using default values from the training data.
- Prediction accuracy depends on the quality and characteristics of the training dataset.
- Predictions are estimates and should not be treated as guaranteed property valuations.

---

## Future Improvements

- Incorporate additional housing datasets.
- Add more property-related input features.
- Improve model performance through further optimization.
- Enhance the user interface and data visualizations.
- Explore additional regression algorithms.
- Improve prediction accuracy using further feature engineering.

---

## Author

**Abdullah Shehzad**

Software Engineering Student | Machine Learning Enthusiast

- GitHub Profile: https://github.com/sezzz7e
- Project Repository: https://github.com/sezzz7e/UrbanNest-Price-Prediction-App
- Live Application: https://urbannest-price-predictor.streamlit.app/

---

Built with Python, Machine Learning, XGBoost, and Streamlit.
