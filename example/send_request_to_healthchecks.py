import requests
try:
    requests.post("https://healthchecks.dev.myovcloud.com/ping/40d5a575-8abe-4bcd-8fad-42a618d332e7", data="testing body", timeout=10)
except requests.RequestException as e:
    print("Ping faild: %s" %e)
