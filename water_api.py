from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///readings.db'

db = SQLAlchemy(app)

class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    level = db.Column(db.Integer)
    temp = db.Column(db.String)


@app.route('/')
def index():
    return str('Hello! /readings for all readings,'
            '/recent for 2 hours of readings, /recent1 for 1 day)'
            '/recent/id for specific id')


@app.route('/readings')
def get_all():
    try: 
        readings = Reading.query.order_by(Reading.id).all()                 
        reading_text = []                  
          
        
        for reading in readings:
            reading_text.append({'id': reading.id, 'time': reading.date, 
            'level': reading.level, 'temperature': reading.temp})                    
            
        return  jsonify(reading_text)

    except Exception as e:            
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text


@app.route('/recent')
def get_last_2_hours():
    try: 
        readings = Reading.query.order_by(Reading.id.desc()).limit(12)
       
        reading_text = []         
            
        
        for reading in readings:
            reading_text.append({'id': reading.id, 'time': reading.date, 
            'level': reading.level, 'temperature': reading.temp})                    
            
        return  jsonify(reading_text)

        
    except Exception as e:            
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
            

@app.route('/recent1')        
def get_last_24_hours():
    try: 
        readings = Reading.query.order_by(Reading.id.desc()).limit(144)
       
        reading_text = []
        
        for reading in readings:
            reading_text.append({'id': reading.id, 'time': reading.date, 
            'level': reading.level, 'temperature': reading.temp})                  

        return  jsonify(reading_text)
    
    except Exception as e:            
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text



@app.route('/recent2')        
def get_last_48_hours():
    try: 
        readings = Reading.query.order_by(Reading.id.desc()).limit(288)
       
        reading_text = []
        
        for reading in readings:
            reading_text.append({'id': reading.id, 'time': reading.date, 
            'level': reading.level, 'temperature': reading.temp})                    
            
        return  jsonify(reading_text)

        
    except Exception as e:            
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text



@app.route('/recent/<id>')
def get_reading(id):
    reading = Reading.query.get_or_404(id)
    return jsonify({'id': reading.id, 'time': reading.date, 
    'level': reading.level, 'temperature': reading.temp,} )


if __name__ == '__main__':
    app.run(debug=True)