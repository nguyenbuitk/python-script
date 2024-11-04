# Weather Forecast Application

This project is a weather forecasting application built with Python and Streamlit. It fetches weather forecast data from the OpenWeatherMap API for a specified city and visualizes the temperature trend over a given number of days.

## Features

- Fetch weather forecast data for any city in the world.
- Display temperature trends for a user-specified number of forecast days.
- Interactive visualization with Streamlit and Plotly.
- Clean and simple interface with options to adjust forecast days and select city.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather_forecast_app.git
   ```
   
2. **Install Required Packages**:
   Ensure you have Python installed. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file should contain:
   ```text
   requests
   pandas
   streamlit
   matplotlib
   plotly
   ```

3. **Set Up API Key**:
   - Sign up on [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
   - Replace the placeholder `API_KEY` in the `main.py` and `test_debug.py` files with your API key.

## Usage

To start the Streamlit application, run the following command in the terminal:

```bash
streamlit run main.py
```

### Interface Overview

1. **City Name**: Enter the city you want the weather forecast for (default is "Ho Chi Minh City").
2. **Forecast Days**: Use the slider to select the number of forecast days (1 to 5).
3. **Data Type**: Currently only supports temperature visualization, but can be extended for more data types.
4. **Temperature Chart**: Displays a line chart showing the temperature trend for the selected forecast period.

### File Descriptions

- **`backend.py`**: Contains `filter_dataframe` function that fetches and processes weather forecast data from OpenWeatherMap API based on the given parameters.
- **`main.py`**: Main file for running the Streamlit app. It creates the interactive interface and displays temperature trends.
- **`test_debug.py`**: Testing script to fetch and display raw weather forecast data for debugging purposes.
- **Weather Icons** (`rain.png`, `snow.png`, `clear.png`, `cloud.png`): Icons representing different weather conditions.

## Example

1. Start the app by running `streamlit run main.py`.
2. Enter the city name, select the forecast days, and choose the data type.
3. The application will display a line chart of the temperature trend for the specified city and period.