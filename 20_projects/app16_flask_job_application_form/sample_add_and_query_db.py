# Example of using flask with flask_sqlalchemy database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.com'

# Create database and associates it with current Flask application
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Check if the script is run directly
if __name__ == "__main__":
    with app.app_context():  # Use app_context to ensure access to the application context
        app.run(debug=True, port=5000)  # Start the Flask development server
        db.create_all()
        new_form = Form(name='John', email='john@sldkjf.com')
        db.session.add(new_form)
        db.session.commit()

        forms = Form.query.all()
        for form in forms:
            print(form.name, form.email)