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
    

if __name__== "__main__":
    app.run(debug=True, host='localhost', port=8000)

