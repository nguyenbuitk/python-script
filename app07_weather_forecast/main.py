import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from backend import filter_dataframe

# Replace with your own OpenWeatherMap API key
API_KEY = '035cbc8aa2af3c9308c97298dae14158'
CITY_NAME = 'Ho Chi Minh City'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

if __name__ == "__main__":
    st.title("Weather Forecast for the Next Days")
    
    place = st.text_input("Place: ", "Ho Chi Minh City")
    forecast_days = st.slider("Forcast Days", 1, 5, 15)
    data_type = st.selectbox("Select data to view", ["Temperature"])
    
    st.subheader(f"{data_type} for the next {forecast_days} days in {place}")
    df = filter_dataframe(API_KEY, place, BASE_URL, forecast_days)

    # Plot the data using Plotly Express
    # Plot the data
    fig = px.line(df, x = "Date", y = 'Temperature', title=f"Temperature by date in {place}")
    st.plotly_chart(fig)
    