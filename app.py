
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st

from pathlib import Path

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="UrbanNest House Price Predictor",
    page_icon="🏡",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "urbannest_best_model.joblib"

METADATA_PATH = BASE_DIR / "model_metadata.json"


# ======================================
# LOAD MODEL AND METADATA
# ======================================

@st.cache_resource
def load_model():

    return joblib.load(MODEL_PATH)


@st.cache_data
def load_metadata():

    with open(METADATA_PATH, "r") as file:

        return json.load(file)


try:

    model = load_model()

    metadata = load_metadata()

except Exception as error:

    st.error("Unable to load the prediction model.")

    st.error(str(error))

    st.stop()


# ======================================
# FEATURE ENGINEERING
# ======================================

def prepare_features(df):

    df = df.copy()

    # These transformations MUST match Task 2.
    # Remove or modify any formula that differs
    # from your original Task 2 feature engineering.

    df["House_Age"] = (
        df["Yr Sold"] - df["Year Built"]
    )

    df["Remodel_Age"] = (
        df["Yr Sold"] - df["Year Remod/Add"]
    )

    df["Total_Bathrooms"] = (
        df["Full Bath"]
        + 0.5 * df["Half Bath"]
        + df["Bsmt Full Bath"]
        + 0.5 * df["Bsmt Half Bath"]
    )

    df["Total_Porch_Area"] = (
        df["Wood Deck SF"]
        + df["Open Porch SF"]
        + df["Enclosed Porch"]
        + df["3Ssn Porch"]
        + df["Screen Porch"]
    )

    df["Total_Finished_Area"] = (
        df["Gr Liv Area"]
        + df["BsmtFin SF 1"]
        + df["BsmtFin SF 2"]
    )

    expected = metadata["feature_columns"]

    missing = [
        col for col in expected
        if col not in df.columns
    ]

    if missing:

        raise ValueError(
            f"Missing model columns: {missing}"
        )

    return df[expected]


# ======================================
# USER INTERFACE
# ======================================

st.title("🏡 UrbanNest")

st.subheader("Smart House Price Prediction")

st.write(
    "Enter property details to generate "
    "an estimated residential property value."
)

st.divider()

st.subheader("Property Information")

defaults = metadata["defaults"]

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Property Details")

        living_area = st.number_input(
            "Living Area (sqft)",
            min_value=200,
            max_value=10000,
            value=1500,
            step=50
        )

        lot_area = st.number_input(
            "Lot Area (sqft)",
            min_value=500,
            max_value=100000,
            value=8000,
            step=100
        )

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=0,
            max_value=15,
            value=3
        )

        full_bath = st.number_input(
            "Full Bathrooms",
            min_value=0,
            max_value=10,
            value=2
        )

        half_bath = st.number_input(
            "Half Bathrooms",
            min_value=0,
            max_value=10,
            value=1
        )

        basement_area = st.number_input(
            "Basement Area (sqft)",
            min_value=0,
            max_value=10000,
            value=1000
        )

    with col2:

        st.markdown("### Quality and Location")

        quality = st.slider(
            "Overall Quality",
            min_value=1,
            max_value=10,
            value=6
        )

        year_built = st.number_input(
            "Year Built",
            min_value=1800,
            max_value=2026,
            value=2000
        )

        year_remodeled = st.number_input(
            "Year Remodeled",
            min_value=1800,
            max_value=2026,
            value=2005
        )

        garage_cars = st.selectbox(
            "Garage Capacity",
            options=[0, 1, 2, 3, 4, 5],
            index=2
        )

        neighborhood = st.selectbox(
            "Neighborhood",
            options=metadata["neighborhood_options"]
        )

        house_style = st.selectbox(
            "House Style",
            options=metadata["house_style_options"]
        )

    submitted = st.form_submit_button(
        "Predict House Price",
        use_container_width=True
    )


# ======================================
# PREDICTION
# ======================================

if submitted:

    try:

        if year_remodeled < year_built:

            st.error(
                "Remodel year cannot be earlier "
                "than the construction year."
            )

            st.stop()

        # Start with training-data defaults.
        property_data = defaults.copy()

        # Override selected features.
        property_data.update({

            "Gr Liv Area": living_area,

            "Lot Area": lot_area,

            "Bedroom AbvGr": bedrooms,

            "Full Bath": full_bath,

            "Half Bath": half_bath,

            "Total Bsmt SF": basement_area,

            "Overall Qual": quality,

            "Year Built": year_built,

            "Year Remod/Add": year_remodeled,

            "Garage Cars": garage_cars,

            "Neighborhood": neighborhood,

            "House Style": house_style

        })

        # Preserve the training dataset's sale year.
        property_data["Yr Sold"] = defaults["Yr Sold"]

        input_df = pd.DataFrame(
            [property_data],
            columns=metadata["raw_input_columns"]
        )

        # Apply the Task 2 transformations.
        model_input = prepare_features(input_df)

        # Predict.
        prediction = float(
            model.predict(model_input)[0]
        )

        if not np.isfinite(prediction) or prediction <= 0:

            raise ValueError(
                "The model generated an invalid price."
            )

        st.success("Prediction generated successfully!")

        st.markdown("### Estimated Property Value")

        st.metric(
            "Predicted House Price",
            f"${prediction:,.2f}"
        )

        st.info(
            "This value is an estimate based on "
            "historical housing data."
        )

        with st.expander("View Property Details"):

            st.dataframe(input_df, use_container_width=True)

    except Exception as error:

        st.error(
            "Unable to generate prediction. "
            "Please verify the property information."
        )

        st.exception(error)


# ======================================
# FOOTER
# ======================================

st.divider()

st.caption(
    "UrbanNest | Machine Learning House Price Prediction"
)
