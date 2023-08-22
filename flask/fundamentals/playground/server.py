from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_level_one():
    return render_template('index.html', num_boxes=3, color='blue')

@app.route('/play/<int:x>')
def play_level_two(x):
    return render_template('index.html', num_boxes=x, color='blue')

@app.route('/play/<int:x>/<color>')
def play_level_three(x, color):
    return render_template('index.html', num_boxes=x, color=color)

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=8000)