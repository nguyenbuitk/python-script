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
    forecast_days = st.slider("Forcast Days", 1, 5)
    data_type = st.selectbox("Select data to view", ["Temperature", "Sky"])
    
    st.subheader(f"{data_type} for the next {forecast_days} days in {place}")
    
    if place:
        try:
            df = filter_dataframe(API_KEY, place, BASE_URL, forecast_days)
            print(df)
            if data_type == "Temperature":
                # Plot the data using Plotly Express
                # Plot the data
                fig = px.line(df, x = "Date", y = 'Temperature', title=f"Temperature by date in {place}")
                st.plotly_chart(fig)
            else:
                image_path_list = []
                for index, row in df.iterrows():
                    image_path = f"images/{row['Description'].lower()}.png"
                    image_path_list.append(image_path)
                    
                st.image(image_path_list, width=115)
                    
        except KeyError:
            st.write("That palace doesn't exist")
    