import requests

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully as {filename}")
    else:
        print("Failed to download the image")

if __name__ == "__main__":
    image_url = "https://s.yimg.com/ny/api/res/1.2/RypT0BOC2tBMqSauT85PnQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTQ4MDtjZj13ZWJw/https://media.zenfs.com/en/Barrons.com/543a7c56d4eb5a4436934e833945fb98"
    filename = "downloaded_image.jpg"
    download_image(image_url, filename)
