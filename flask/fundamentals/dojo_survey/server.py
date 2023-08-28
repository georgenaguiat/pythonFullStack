from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'this is a secret key'

@app.route('/', methods=['GET', 'POST'])
def survey():
    locations = ['Select A Location','Las Vegas', 'Chicago', 'Arizona', 'New York', 'Texas']
    languages = ['Select A Language','HTML', 'CSS', 'JavaScript', 'Python', 'C#']
    if request.method == 'POST':
        session['name'] = request.form['name']
        selected_location = request.form['dojo_location']
        session['selected_location'] = selected_location
        selected_languages = request.form['favorite_language']
        session['selected_languages'] = selected_languages
        session['comments'] = request.form['comments']
        return redirect(url_for('result'))

    return render_template('dojo_survey.html', locations=locations, languages=languages)

@app.route('/result')
def result():
    return render_template('result.html', name=session.get('name'), selected_location=session.get('selected_location'),
                            selected_languages=session.get('selected_languages'), comments=session.get('comments'))

@app.route('/back')
def back():
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=8000)