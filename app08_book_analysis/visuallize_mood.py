import os
import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

folder_path = "diary/"
file_names = sorted(os.listdir(folder_path))
analyzer = SentimentIntensityAnalyzer()
dates = []
negativity = []
positivity = []
for filename in file_names:
    # Check if item is a file
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        # Open the file and read its content
        with open(file_path, "r") as file:
            content = file.read()
            scores = analyzer.polarity_scores(content)
            positivity.append(scores["pos"])
            negativity.append(scores["neg"])
            date = file_path.strip(".txt").strip("diary/")
            dates.append(date)

print(dates)
print(negativity)
print(positivity)

st.title("Diary Tone")
st.subheader("Positivity")

pos_figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

