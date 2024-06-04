import streamlit as st
import numpy as np
import pandas as pd

st.title('Simple Streamlit App')

user_name = st.text_input('Enter your name')

user_age = st.number_input('Enter your age', min_value=0, max_value=100)

user_experience = st.slider('Rate you programming experience', 0, 10, 5)

if st.button('Submit'):
    st.write(f"Hello {user_name}, you are {user_age} years old and rated your promgramming {user_experience}")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
