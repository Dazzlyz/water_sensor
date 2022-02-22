from ast import dump
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import os
import json

# fix database in own file + class
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///readings.db'

db = SQLAlchemy(app)

class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)

@app.route('/')
def index():
    try: 
        readings = Reading.query.order_by(Reading.id).all()           
        reading_text = {
            'ID' : [],            
        }     
        
        for reading in readings:
            reading_text['ID'].append({reading.id : reading.level})
                     
            
        return  jsonify(reading_text)

    except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)