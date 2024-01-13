import requests

files = {'file': open('image.png', 'rb')}
r = requests.post('https://enolzi8ie53r.x.pipedream.net/post', files=files)

files_explicit = {'file': ('image.png', open('image.png','rb'), 'image/png')}
r = requests.post('https://enolzi8ie53r.x.pipedream.net/post', files=files_explicit)
