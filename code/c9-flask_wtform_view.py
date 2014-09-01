from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from c8_flask_wtf import MyForm


app = Flask(__name__)
app.secret_key = 'itmard_khastas:D'
Bootstrap(app)

@app.route('/submit/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'success'
    return render_template('submit.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
