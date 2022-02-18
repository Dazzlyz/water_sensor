from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)

@app.route('/')
def index():
    return 'Welcome!'

@app.route('/levels')
def get_readings():
    readings = Levels.query.all()

    output =[]
    for reading in readings:
        level_data = {'level': reading.level}
        	
        output.append(level_data)
    return json.dumps(output)

@app.route('/levels/<id>')
def get_reading(id):
    reading = Levels.query.get_or_404(id)
    return {'level' : Levels.level}

@app.route('/levels', methods=['POST'])
def add_level():
    level = Levels(level=request.json['level'])
    db.session.add(level)
    db.session.commit()
    return {'id': level.id}

if __name__ == '__main__':
    app.run(debug=True)