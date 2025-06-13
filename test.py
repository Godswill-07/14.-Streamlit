import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


data = {
    "wake_hour": [7,6,6.25,6.50,7.25],
    "work_hours": [8,7,6,8,8.25],
    "screen_time": [5,6,5,6.75,7],
    "sleep_time": [23.25,23,23.50,22.75,23]
}

df = pd.DataFrame(data)
X = df[["wake_hour", "work_hours", "screen_time"]]
y = df["sleep_time"]

model = RandomForestRegressor()
model.fit(X,y)

st.title("Sleep Time Predictor")

st.write("Welcome Master Godswill, Please enter your daily routine and we will predict your ideal sleep time ")

wake_hour = st.slider("When did you wake up today(Hour, 24H)",5.0,8.0,2.0, step=0.25)
work_hours = st.slider("How many hours did you work today",0.0,9.0,2.0, step=0.25)
screen_time = st.slider("How many hours of screen time did you have today?",0.0,9.0,2.0, step=0.25)

if st.button("Predict Sleep Time"):
    input_data = [[wake_hour, work_hours, screen_time]]
    predicted_sleep = model.predict(input_data)[0]

    def time_float_to_str(t):
          h = int(t) % 24 #takes the input 
          m = int((t - int(t)) * 60)
          return f"{h:02d}:{m:02d}" #pad with zero, if the number is less than 2 digits, its to display 2digits in the hour and mins

    sleep_time_str = time_float_to_str(predicted_sleep)
    st.success(f"Based on your inputs, you may sleep around {sleep_time_str}")