# This script uses Streamlit to create a webpage that displays a photo, a biography, and list of python apps including description, iamges and source code links.

import pandas 
import streamlit as st
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'data.csv')
st.set_page_config(layout="wide")
# Set the title of the page
st.title("Portfolio of Nguyen Bui")
st.write("**Welcome to personal portfolio!** This web is built with streamlit, and it show my python project")

# Create two columns
col1, col2 = st.columns([1,2])

# Display the image in the first column
with col1:
    st.image(f"{current_directory}/images/10.png", caption="Nguyen Bui", use_column_width=True)

# Display the biography text in the second column
with col2:
    st.subheader("Introduce")
    st.write("""
    Hi, I am Nguyen Bui! a DevSecOps engineer with over 3 years of experience
    """)
    
st.write("---")
st.header("My project")

col3, emptycol, col4 = st.columns([1.5, 0.1, 1.5])

df = pandas.read_csv(csv_file_path, sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(f"📌 {row['title']}")
        st.write(row["description"])
        st.image(f"{current_directory}/images/" + row["image"], use_column_width=True)
        st.markdown(f"[Source Code]({row['url']})")
        st.write("---")  
        
with col4: 
    for index, row in df[10:].iterrows():
        st.subheader(f"📌 {row['title']}")
        st.write(row["description"])
        st.image(f"{current_directory}/images/" + row["image"], use_column_width=True)
        st.markdown(f"[Source Code]({row['url']})")
        st.write("---")  