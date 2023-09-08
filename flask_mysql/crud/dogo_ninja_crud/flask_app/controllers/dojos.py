from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    show_all_dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', show_all_dojos=show_all_dojos)

@app.route('/dojo', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def get_dojo_with_ninja(dojo_id):
    dojo = Dojo.get_one_dojo(dojo_id)
    ninjas = Dojo.dojo_with_ninjas(dojo_id)
    return render_template('dojo_show.html', get_dojo=dojo, get_ninjas=ninjas)
