# an object of WSGI application
from flask import Flask
# Flask constructor
app = Flask(__name__)

# A decorator (@app.route()) used to tell the application which URL is associated function
# url '/' (localhost:5000) associate with hello_world() function
# / ~ localhost:5000 + / = localhost:5000/
# /secondpage/ ~ localhost:5000 + /secondpage/ = localhost:5000/secondpage/
@app.route('/')
def hello_world():
    return 'HELLO'
# app.add_url_rule('/', 'hello', hello_world) có thể được thay thế cho @app.route('/')

# url '/secondpage/' (localhost:5000/secondpage)
# associate with after_hello() function
@app.route('/secondpage/')
def after_hello():
    return 'This page is after hello page'


if __name__ == '__main__':
    app.run()
