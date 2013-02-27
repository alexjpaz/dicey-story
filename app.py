import os

from flask import Flask, url_for,render_template, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from flask import jsonify

from collections import OrderedDict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/assets/<path:filename>')
def assets(filename):
    return	send_from_directory('static/assets', filename)
    
@app.route('/game/', methods=['POST'])
def add_game():
    print request
    
    
@app.route('/game/<game_id>')
@app.route('/game/', defaults={'game_id': None})
def get_games(game_id):
    if game_id == None:
        games = []
        
        for g in Game.query.all():
            games.append(g._asdict())
            
        json = jsonify(games=games)
            
    else:
        game = Game.query.get(game_id)
        
        if game == None:
            return 404
        
        json = jsonify(game._asdict())
    
    return json    



class DictSerializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name
    

class Game(db.Model, DictSerializable):
    id = db.Column(db.Integer, primary_key=True)
    dicechars = db.Column(db.Text)
    fontset = db.Column(db.String(80))

    def __init__(self, dicechars, fontset):
        self.dicechars = dicechars
        self.fontset = fontset
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=port)










