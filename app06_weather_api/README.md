# Weather Data API
The project is a Weather API application built using Python and Flask. It allows users to fetch and display weather data. The repository includes the main application file (main.py), which handles the logic for retrieving and presenting weather information, and templates for the web interface. The data_small folder contains sample data, while static and templates folders hold static files and HTML templates, respectively.

## Features

- Display a list of meteorological stations with their names and IDs.
- API endpoints to retrieve temperature data:
  - **Single Date**: Get temperature for a specific station on a specific date.
  - **All Data**: Retrieve all temperature records for a specific station.
  - **Yearly Data**: Retrieve temperature records for an entire year for a specific station.

## How to run
- python3 main.py
- streamlit run visualize.py