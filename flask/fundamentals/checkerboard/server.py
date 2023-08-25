from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/')
def checker():
    return render_template('checkerboard.html', rows=8)

@app.route('/<int:x>')
def checker_box(x):
    return render_template('checkerboard.html', rows=x)

if __name__=='__main__': # Ensure this file is being run directly and not from a different module
    app.run(debug=True, host="localhost", port=8000)