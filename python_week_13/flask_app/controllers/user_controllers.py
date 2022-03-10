from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/register', methods=['POST'])
def register_user():
    data = {
        'name' : request.form['name'],
        'user_name' : request.form['user_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
    }
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(request.form['password'])
    # print(pw_hash)
    data['pw_hash'] = pw_hash
    valid = User.user_validator(data)
    if valid :
        user = User.create_user(data)
        # Checks the user in session
        session['user_id'] = user
        print('You got it, You are a new user')
        return redirect('/travels')
    # print(valid)
    # user = User.create_user(data)
    # return redirect('/success')
    return redirect('/travels')

@app.route('/user/login', methods=['POST'])
def login_user():
    user = User.get_by_email(request.form)
    if not user:
        flash('Invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid email or password')
        return redirect('/')
    session['user_id'] = user.id
    print('Success')
    return redirect('/travels')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')