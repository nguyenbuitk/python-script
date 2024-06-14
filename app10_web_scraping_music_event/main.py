import requests
import selectorlib
import sqlite3
from datetime import datetime
import smtplib, ssl

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {

}

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "buinguyen23112k@gmail.com"
    password = "xivsnaecgqkgctpj"

    receiver = "buinguyen23112k@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

# this function using selectorlib to get specific id of html web page
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

# store tempearature and to file
def store_to_file(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        line = "{},{}\n".format(now,extracted)
        file.write(line)


def store_to_db(extracted):
    connection = sqlite3.connect("data.db")
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?, ?)", (now, extracted))
    connection.commit()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print("temperature now:", extracted)
    store_to_db(extracted)
    # send_mail(message="New event occurs")