import requests
from send_mail import send_mail

topic = "vietnamese"

api_key = "0c6d60564cb04ff4a3869ae2d32eac5d"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
    "from=2024-10-20&sortBy=popularity&apiKey=" \
    "0c6d60564cb04ff4a3869ae2d32eac5d&language=en"

request = requests.get(url)
content = request.json()
with open("tmp.txt", "w") as f:
    f.write(str(content["articles"][:5]))
    

body = "Subject: Today's news" + "\n"
for article in content["articles"][:5]:
    if article["title"] is not None: 
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n" + 70*"-" +  2*"\n"

body = body.encode("utf-8")
send_mail(message=body)