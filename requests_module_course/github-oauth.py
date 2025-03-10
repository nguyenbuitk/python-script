import requests
from flask import Flask, request

CLIENT_ID = '6594b05d42bde7721080'
CLIENT_SECRET = 'e4dfc9b285a95bc299239ad3fb8d0afe3780814b'
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
BASE_URL = 'https://api.github.com'
app = Flask(__name__)

@app.route('/')
def index():
    # step 1 and 2: GET /login/github and redirect to github.com
    return '<a href="https://github.com/login/oauth/authorize?client_id={}">Login with Github</a>'.format(CLIENT_ID)

    # step 3: github response for login and to authorize application
    # step 4: login successful and app authorized
@app.route('/authorize')
def authorize():
    print("URL: ", request.url)
    # step 5: code return
    code = request.args.get('code')
    headers = {'Accept' : 'application/json'}
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    
    # step 6: request for user data containing the CODE, and github oauth credentials
    r = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers)
    token = r.json()['access_token']
    headers2 = {'Authorization': 'token ' + token}
    # headers['Authorization'] = 'token {}'.format(token)

    # step 7: user data returned
    r2 = requests.get(BASE_URL + '/user/repos', headers=headers2)
    print(r2.json()[0]['name'])
    repos = r2.json()
    list_of_repos = []
    for repo in repos:
        list_of_repos.append(repo['name'])
    print(list_of_repos)

    return '<br>'.join(list_of_repos)

if __name__ == '__main__':
    app.run(debug=True)