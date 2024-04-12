from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime



app = Flask(__name__)
app.secret_key = 'development key'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="nervles",
    password="alamakota", # database passowrd hidden
    hostname="nervles.mysql.pythonanywhere-services.com",
    databasename="nervles$weather_station",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299 # connection timeouts
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # no warning disruptions

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Weather_station(db.Model):

    __tablename__ = "weather_station"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    location = db.Column(db.String(4096))


    def __init__(self, name, location):
        self.name = name
        self.location = location

class Weather_stationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id' ,'name', 'location')



weather_station_schema = Weather_stationSchema()
weather_stations_schema = Weather_stationSchema(many=True)


class Mes(db.Model):

    __tablename__ = "mes"
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    created_at = db.Column(db.DATETIME)
    device_id = db.Column(db.Integer)


    def __init__(self, temperature, humidity, created_at, device_id):
        self.temperature = temperature
        self.humidity = humidity
        self.created_at = created_at
        self.device_id = device_id

class MesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'temperature', 'humidity', 'created_at', 'device_id')




mes_schema = MesSchema()
meses_schema = MesSchema(many=True)




@app.route("/weather_station/<id>", methods=["GET"])
def get_weather_station_by_one(id):
    weather_station = Weather_station.query.get(id)
    result = weather_station_schema.dump(weather_station)
    return jsonify(result)

@app.route("/weather_stations", methods=["GET"])
def get_weather_stations():
    weather_stations = Weather_station.query.all()
    result = weather_stations_schema.dump(weather_stations)
    return jsonify(result)

@app.route("/add/station", methods=["POST"])
def post_station():
    name = request.json["name"]
    location = request.json["location"]
    new_weather_station = Weather_station(name, location)
    db.session.add(new_weather_station)
    db.session.commit()
    weather_station = Weather_station.query.get(new_weather_station.id)
    result = weather_station_schema.dump(weather_station)
    return jsonify(result)

@app.route("/mes/<id>", methods=["GET"])
def get_mes_by_one(id):
    mes = Mes.query.get(id)
    result = mes_schema.dump(mes)
    return jsonify(result)

@app.route("/mes", methods=["GET"])
def get_mes():
    mes = Mes.query.all()
    result = meses_schema.dump(mes)
    return jsonify(result)

@app.route("/add/mes", methods=["POST"])
def post_mes():
    temperature = request.json["temperature"]
    humidity = request.json["humidity"]
    #created_at = request.json["created_at"]
    device_id = request.json["device_id"]
    new_mes = Mes(temperature, humidity, datetime.now(), device_id)
    db.session.add(new_mes)
    db.session.commit()
    mes = Mes.query.get(new_mes.id)
    result = mes_schema.dump(mes)
    return jsonify(result)


@app.route("/web/<device_id>", methods=["GET"])
def get_mes_database(device_id):
    all_mes = Mes.query.filter_by(device_id=device_id).order_by(Mes.created_at.desc()).all()
    result = meses_schema.dump(all_mes)
    return render_template('dane.html', title=f'Weather Station Measurements for Device {device_id}', measurements=result)

@app.template_filter('datetimefmt')
def datetime_format(value, format='%Y-%m-%d %H:%M:%S'):
    if isinstance(value, str):
        # Przekształć ciąg znaków na obiekt datetime
        value = datetime.fromisoformat(value)
    return value.strftime(format)



@app.route('/z')
def hello_world():
    return 'Pozdrawiam!!!'
