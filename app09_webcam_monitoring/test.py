import cv2
import streamlit as st

def main():
    st.title("Video Stream Demo")

    # Initialize session state
    if "start_button" not in st.session_state:
        st.session_state.start_button = False

    # Create a start button
    start_button = st.button("Start Video")

    if start_button:
        # Set start_button attribute to True
        st.session_state.start_button = True

    if st.session_state.start_button:
        # Start capturing video
        video_capture = cv2.VideoCapture(0)

        # Create an empty placeholder for the video frame
        video_placeholder = st.empty()

        while st.session_state.start_button:
            ret, frame = video_capture.read()
            if not ret:
                st.error("Failed to capture video.")
                break

            # Convert the frame to RGB color format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame on the web page
            video_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

            # Check if the start button is still pressed
            if not st.session_state.start_button:
                break

        # Release the video capture object
        video_capture.release()

if __name__ == "__main__":
    main()
