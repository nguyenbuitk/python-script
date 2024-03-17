import requests
from send_mail import send_mail

topic = "tesla"

api_key = "72ad054290d64d5f847f4a95df8a631f"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
    "from=2024-02-16&sortBy=publishedAt&apiKey=" \
    "72ad054290d64d5f847f4a95df8a631f&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None: 
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n" + 70*"-" +  2*"\n"

body = body.encode("utf-8")
send_mail(message=body)