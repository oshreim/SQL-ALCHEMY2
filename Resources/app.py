import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# ======================DATABASE=SETUP=====================
engine=create_engine('sqlite:///hawaii.sqlite')
Base=automap_base()
Base.prepare(engine,reflect=True)
Measurement=Base.classes.measurement
Station=Base.classes.station
session = Session(engine)

# =====================Flask Setup =======================
app= Flask(__name__)

Nav =  '''<div class='titleDiv'></div>
        <h1>welcome to the Hawaii Climate Analysis API!</h1>
        <div class='mainDiv'>
            <h2>Available Routes:</h2>
            <ul>
                <li><a href='/api/v1.0/precipitation'>Precipitation</a></li>
                <li><a href='/api/v1.0/stations'>Stations</a></li>
                <li><a href='/api/v1.0/tobs'>Tobs</a></li>
                <li><a href='/api/v1.0/temp/2017-06-01/2017-06-15'>Change start and end date</a></li>
            </ul>
        </div>
        <style>
            body { background: cadetblue; }
            h1 { text-align: center }
            .titleDiv {
                background-image:url('https://i.ytimg.com/vi/CmbDvX47SRw/maxresdefault.jpg');
                background-size:100% 40vh;
                height:35vh;
                background-repeat:no-repeat;
                margin: -10px;
                }
            .responseDiv {
                background: white;
                width: fit-content;
                margin: auto;
                height: 30vh;
                overflow: auto;
                padding: 5px;
                border: 1px solid;
                box-shadow: 3px 3px 7px;
            }
            .mainDiv { width: fit-content; margin: auto}
        </style>'''
    
# ============ Routes =================

@app.route('/')
def welcome(): 
    return Nav


@app.route('/api/v1.0/precipitation')
def precipitation(): 
    prev_year=dt.date(2017,8,23)-dt.timedelta(365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=prev_year).all()

    precip = ''
    for date, prcp in precipitation:
        precip += f'{date}: {prcp} <br/>'
    return precip

# @app.route('/api/v1.0/precipitation')
# def precipitation(): 
#     return Nav


if __name__ == '__main__':
    app.run()