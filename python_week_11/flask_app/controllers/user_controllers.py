from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'date_of_birth' : request.form['date_of_birth'],
        'password' : request.form['password'],
    }
    valid = User.user_validator(data)
    if valid:
        results = User.create_user(data)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:id>')
def get_one(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('results.html', user = user)