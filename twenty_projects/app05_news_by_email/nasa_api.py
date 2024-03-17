import requests
import streamlit as st

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully as {filename}")
    else:
        print("Failed to download the image")

api_key = "YSYzxjr0coojssNUobL61aH2s4bzZAXtuGelSmQp"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

download_image(content["hdurl"], "astronomy.jpg")

st.title(content["title"])
st.image("astronomy.jpg")
st.write(content["explanation"])

