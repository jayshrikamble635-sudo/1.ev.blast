import streamlit as st
import pandas as pd
import joblib

st.title("EV Blast Prediction System")

# Load trained model
model = joblib.load("dtc_model (1).pkl")

st.subheader("Enter Vehicle Details")

# Automatically create inputs based on model features
input_data = {}

for feature in model.feature_names_in_:
    input_data[feature] = st.number_input(feature, value=0.0)

if st.button("Predict"):
    try:
        df = pd.DataFrame([input_data])
        prediction = model.predict(df)

        if prediction[0] == 1:
            st.error("High Risk of EV Blast")
        else:
            st.success("EV is Safe")

    except Exception as e:
        st.error("Something went wrong")
        st.write(e)
