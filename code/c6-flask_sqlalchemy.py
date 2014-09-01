from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

db.create_all()

#http://127.0.0.1:5000/show_user_from_db/?username=itmard&email=mrkamalifard@gmail.com
@app.route('/show_user_from_db/')
def show_user():
	if request.args.get('username') and request.args.get('email'):
		user = User(username=request.args.get('username'), email=request.args.get('email'))
		db.session.add(user)
		db.session.commit()
		
	return str([user_from_db.username for user_from_db in User.query.all()])


if __name__ == '__main__':
	app.run(debug=True)