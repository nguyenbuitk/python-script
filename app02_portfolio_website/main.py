# This script uses Streamlit to create a webpage that displays a photo, a biography, and list of python apps including description, iamges and source code links.

import pandas 
import streamlit as st
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'data.csv')
st.set_page_config(layout="wide")
# Set the title of the page
st.title("Nguyen Bui")

# Create two columns
col1, col2 = st.columns(2)

# Display the image in the first column
with col1:
    st.image(f"{current_directory}/images/10.png", caption="Ardit Sulce", use_column_width=True)

# Display the biography text in the second column
with col2:
    st.write("""
    Hi, I am Nguyen Bui! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing. I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """)

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv(csv_file_path, sep=";")
print(type(df))
print(df)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"{current_directory}/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4: 
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"{current_directory}/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        