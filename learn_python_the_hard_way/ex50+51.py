from flask import Flask
from flask import render_template
from flask import request

# request.args.get(key, default = None, type = none)

template_dir = 'D://Document//Code//Python//LearnPythonTheHardWay//projects//gothonweb//templates'
app = Flask(__name__,template_folder = template_dir)
@app.route("/hello")
def index():
    name_app = request.args.get('name_web')                 # lấy name_web từ web
    name_app2 = request.args.get('name_web2', 'Hai Yen')    # default là hai yen khi không truyền vào

    if name_app:
        greeting_app = f"Hello, {name_app}, and {name_app2}"
    else:
        greeting_app = "Hello World"
        
    return render_template("index.html", greeting= greeting_app)

if __name__ == "__main__":
        app.run()