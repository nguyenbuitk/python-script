import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px

st.write("Explore temperature by station and date range.")
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations_name = stations[['STANAME                                 ']]
station_name = st.selectbox("Choose stations", stations_name.values)
station_id = stations.loc[stations['STANAME                                 '] == station_name]['STAID'].values[0]

station = pd.read_csv(f"data_small/TG_STAID{str(station_id).zfill(6)}.txt",skiprows=20,parse_dates=['    DATE'])
station = station.loc[station['   TG'] != -9999]
station['   TG'] = station['   TG']/10

min_date = station['    DATE'].min()
max_date = station['    DATE'].max()
print(min_date)
print(max_date)
start_date = st.date_input("Select start date", min_value=min_date, max_value=max_date)
print(type(start_date))
end_date = st.date_input("Select end date", min_value=start_date, max_value=max_date)

st.write(f"Data for {station_name}")
station = station[(station['    DATE'].dt.date > start_date) & (station['    DATE'].dt.date < end_date)]
station
st.write("Temperature per station")
st.line_chart(data=station, x='    DATE', y='   TG')