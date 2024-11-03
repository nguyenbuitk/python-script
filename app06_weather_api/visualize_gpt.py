import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the stations data and allow user to select a station
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

st.title("Weather Data Visualization")
st.write("Explore temperature data by station and date range.")

# Select station
station_name = st.selectbox("Select a station:", stations["STANAME                                 "].values)
station_id = stations.loc[stations["STANAME                                 "] == station_name, "STAID"].values[0]

# Load data for the selected station
filename = f"data_small/TG_STAID{str(station_id).zfill(6)}.txt"
df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
df.rename(columns={"    DATE": "Date", "   TG": "Temperature"}, inplace=True)
df["Temperature"] = df["Temperature"] / 10  # Convert temperature to °C

# Date range filter
start_date = st.date_input("Start date", min_value=df["Date"].min(), max_value=df["Date"].max())
end_date = st.date_input("End date", min_value=start_date, max_value=df["Date"].max())
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# Show table of filtered data
st.subheader(f"Data for {station_name}")
st.write(filtered_df)

# Plot temperature data
st.subheader("Temperature Trend")
plt.figure(figsize=(10, 5))
plt.plot(filtered_df["Date"], filtered_df["Temperature"], marker='o', linestyle='-', color='b')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Trend at {station_name}")
plt.grid(True)
st.pyplot(plt)
