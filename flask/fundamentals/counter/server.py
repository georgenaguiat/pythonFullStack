from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep this secret and safe'


@app.route('/')
def main():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('counter.html', counter=session['counter'])

@app.route('/destory_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/count/<int:count>')
def count_by_two(count):
    session['counter'] += count
    return redirect('/')
    

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=8000)