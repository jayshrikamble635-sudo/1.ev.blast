

import streamlit as st
import pandas as pd
import joblib

st.title("EV Blast Prediction System")

# Model Load
model = joblib.load("dtc_model (1).pkl")   # apna model file name yaha likho

st.subheader("Enter Vehicle Details")

battery_temp = st.number_input("Battery Temperature", min_value=0.0)
voltage = st.number_input("Voltage", min_value=0.0)
current = st.number_input("Current", min_value=0.0)
charging_cycles = st.number_input("Charging Cycles", min_value=0)
input_data = pd.DataFrame({
        "battery_temp": [battery_temp],
        "voltage": [voltage],
        "current": [current],
        "charging_cycles": [charging_cycles]
    })
input_data.columns = model.feature_names_in_
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("High Risk of EV Blast")
    else:
        st.success("EV is Safe")
