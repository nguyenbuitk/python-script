import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

    #name = request.args.get('name', 'Nobody')
    #greet = request.args.get('greet', 'Hello')

    #if name:
    #        greeting = f"{greet},{name}"
    #else:
    #        greeting = "Hello World"

    #return render_template("index.html", greeting=greeting)

# File Upload
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploaded_files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'fileToUpload' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['fileToUpload']

        # if user does not selecte file, browser also submit an empty part
        # without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # only if file exists and allowed_file is true run the below
        if file and allowed_file(file.filename):
                # secure_filename used to make sure user can not hack server
                # by pointing to a potential file on the server
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file', filename=filename))
    return render_template('file_upload.html')

# Serve uploaded files
@app.route('/uploaded_files/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run()
