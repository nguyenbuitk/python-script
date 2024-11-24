import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



def filter_dataframe(apikey, city_name, base_url, forecast_date):
    # Make the API request
    params = {
        'q': city_name,
        'appid': apikey,
        'units': 'metric'  # Use 'metric' to get temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract relevant data
    forecast_list = data['list']
    print("forcast_list:", type(forecast_list))
    # return list time [3h, 6h, 9h, 12h, 15h, ...]
    # get forecast date <=> get last forecast_date*8 element
    dates = [item['dt_txt'] for item in forecast_list][:forecast_date*8]
    temperatures = [item['main']['temp'] for item in forecast_list][:forecast_date*8]
    descriptions = [item['weather'][0]['main'] for item in forecast_list][:forecast_date*8]

    # Create a DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Temperature': temperatures,
        'Description': descriptions
    })
    
    return df
    # Display the DataFrame

if __name__ == "__main__":
    filter_dataframe("1e4f358eb16a06a534c9fe3bd9d93ce7", "Ho Chi Minh City", "http://api.openweathermap.org/data/2.5/forecast", 3)