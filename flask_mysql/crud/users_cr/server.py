from flask import Flask, render_template, request, redirect, url_for
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route('/')
def all_users():
    users = User.get_all_user()
    return render_template("read_all.html", users=users)

@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('new_user.html')
    if request.method == 'POST':
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email']
        }
    User.save(request.form)
    return redirect('/')

@app.route('/user/show/<int:user_id>')
def show_user(user_id):
    data = {
        'id': user_id
    }
    return render_template('show.html', get_user=User.get_one(data))

@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    data = {
        'id': user_id
    }
    return render_template('edit.html', edit_user = User.get_one(data))

@app.route('/user/update/<int:user_id>', methods=['POST'])
def update(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/user/show/{user_id}')

@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    data = {
        'id': user_id
    }
    User.destroy(data)
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True, host='localhost', port=8000)

