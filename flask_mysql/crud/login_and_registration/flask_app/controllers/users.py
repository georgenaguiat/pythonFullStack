from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('registration_login.html')

@app.route('/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    users = User.get_all_users()
    return render_template('display_user.html', users=users)

@app.route('/register', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if User.user_login(request.form):
        return redirect('/dashboard')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')