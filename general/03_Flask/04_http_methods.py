from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        # nm is name of form field
        # If the method is POST, it means that a form was submitted. In this case, the value entered in the form field with the name nm is retrieved using request.form['nm'].
        user = request.form['nm']
        # the function redirects the user to the success route using redirect(url_for('success', name=user)). The name parameter is passed to the success route, allowing it to access and display the value of nm.
        print("post", user)
        return redirect(url_for('success', name = user))
    else:
        # the value of the nm parameter from the query string (URL parameters) is retrieved using request.args.get('nm').
        user = request.args.get('nm')
        print(user)
        return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.run(debug = True)
