# Diary Tone Analyzer
## Overview
This repository is a sentiment analysis tool designed to evaluate and visualize the emotional tone of personal diary entries. By levaraging natural language processing (NLP), the application provides insights into positivity and negativity trends over time, enabling users to better understand their emotional journey

## Features
- Sentiment Analysis
    + Utilizeds `nltk.sentiment` for evaluating the emotional tone of each diary entry.
    + Analyzes positivity and negativity scores for each file
- Visualization:
    + Generates interactive line charts using Plotly to depict trends in positivity and negativity over time
- Stramlit Dashboard:
    + User-friendly dashboard to display the sentiment analysis results

## Core Files
`main.py` and `visualize_mood.py`:
- Both scripts analyze text fiels from a "diary" folder, extract sentiment scores using the NLTK SentimentIntensityAnalyzer, and plot the results as interactive line charts using Plotly in a Streamlit app