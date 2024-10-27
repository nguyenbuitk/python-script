import streamlit as st
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.header("Column 1")
    st.write("This is some text in column 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("Column 2")
    st.write("This is some text in column 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("Column 3")
    st.write("This is some text in column 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")