import requests
import selectorlib

from datetime import datetime

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {

}

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("./extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        line = "{}: {} degree celsius\n".format(now,extracted)
        file.write(line)

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print("temperature now:", extracted)
    store(extracted)