import requests
r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)

with open('image.png', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)