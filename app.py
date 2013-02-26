import os

from flask import Flask, url_for,render_template, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/assets/<path:filename>')
def assets(filename):
    return	send_from_directory('static/assets', filename)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name
    

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dicechars = db.Column(db.String(120))
    fontset = db.Column(db.String(80))

    def __init__(self, dicechars, fontset):
        self.dicechars = name
        self.fontset = email

    def __repr__(self):
        return '<Game %r, %r>' % (self.name, self.fontset)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=port)










