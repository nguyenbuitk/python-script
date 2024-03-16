import requests
from send_mail import send_mail

api_key = "72ad054290d64d5f847f4a95df8a631f"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2024-02-16&sortBy=publishedAt&apiKey=" \
    "72ad054290d64d5f847f4a95df8a631f"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None: 
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_mail(message=body)