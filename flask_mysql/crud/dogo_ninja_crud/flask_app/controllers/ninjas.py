from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models import dojo


@app.route('/ninja')
def index_ninja():
    return render_template('ninja.html')

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    Ninja.save_ninja(request.form)
    return redirect('/')

@app.route('/ninjas')
def dojos():
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template('ninja.html', all_dojos=all_dojos)