from flask import Flask
from flask import render_template
from flask import request

# request.args.get(key, default = None, type = none)

template_dir = 'D://Document//Code//Python//LearnPythonTheHardWay//projects//gothonweb//templates'
app = Flask(__name__,template_folder = template_dir)
@app.route("/hello", methods = ['POST', 'GET'])             # post là điền vào url

def index():                                                # get là lấy từ khung

    # greeting = "hello world"
    # if request.methods == 'post':
        # #name = request.form['name']
        # #greet = request.form['greet']
        # name = request.args.get('name')
        # name2 = request.args.get('name2')
        # greeting = f"{name}, {name2}"
        # return render_template("index.html", greeting = greeting)
    #else:   # get
        #return render_template("hello_form.html")
    pass

if __name__ == "__main__":
        app.run()