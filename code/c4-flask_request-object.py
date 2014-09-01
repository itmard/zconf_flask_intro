from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'itmard_khastas:D'
Bootstrap(app)

@app.route('/')
def index():
    login_status = session.get('logged_in')
    return render_template('index.html', login_status=login_status)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' and request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            session['logged_in'] = True
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout/')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = False
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)