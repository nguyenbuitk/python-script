import streamlit as st

if st.button("Say Hello"):
    st.write("Say hello is clicked")
else: st.write("Press the button to greet")

if st.button("Toggle Message"):
    if "show_message" not in st.session_state:
        st.session_state.show_message = True
    else: st.session_state.show_message = not st.session_state.show_message

if st.session_state.get("show_message"):
    st.write("This is toggled message, Click the button again to hide it")
st.session_state