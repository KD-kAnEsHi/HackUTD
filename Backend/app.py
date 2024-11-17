import os
from flask import Flask, Response, request, jsonify, make_response
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Setup MongoDB connection
mongo_db_url = os.environ.get("MONGO_DB_CONN_STRING")
client = MongoClient(mongo_db_url)
db = client['sensors_db']

# Root route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Sensors API",
        "endpoints": {
            "GET/POST": "/api/sensors_db/sensors",
            "PUT/DELETE": "/api/sensors_db/sensors/<id>"

        }
    })

@app.get("/api/sensors_db/sensors")
def get_sensors():
    sensor_id = request.args.get('sensor_id')
    filter = {} if sensor_id is None else {"sensor_id": sensor_id}
    sensors = list(db.sensors.find(filter))
    response = Response(
        response=dumps(sensors),
        status=200,
        mimetype="application/json"
    )
    return response

@app.post("/api/sensors_db/sensors")
def add_sensor():
    _json = request.json
    if not _json:
        return make_response(jsonify({"error": "Invalid request data"}), 400)
    
    db.sensors.insert_one(_json)
    resp = jsonify({"message": "Sensor added successfully"})
    resp.status_code = 200
    return resp

@app.delete("/api/sensors_db/sensors/<id>")
def delete_sensor(id):
    try:
        result = db.sensors.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return make_response(jsonify({"error": "Sensor not found"}), 404)
        
        resp = jsonify({"message": "Sensor deleted successfully"})
        resp.status_code = 200
        return resp
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.put("/api/sensors_db/sensors/<id>")
def update_sensor(id):
    _json = request.json
    if not _json:
        return make_response(jsonify({"error": "Invalid request data"}), 400)
    
    try:
        result = db.sensors.update_one(
            {'_id': ObjectId(id)},
            {"$set": _json}
        )
        if result.matched_count == 0:
            return make_response(jsonify({"error": "Sensor not found"}), 404)
        
        resp = jsonify({"message": "Sensor updated successfully"})
        resp.status_code = 200
        return resp
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.errorhandler(400)
def handle_400_error(error):
    return make_response(jsonify({
        "errorCode": error.code,
        "errorDescription": "Bad request!",
        "errorDetailedDescription": error.description,
        "errorName": error.name
    }), 400)

@app.errorhandler(404)
def handle_404_error(error):
    return make_response(jsonify({
        "errorCode": error.code,
        "errorDescription": "Resource not found!",
        "errorDetailedDescription": error.description,
        "errorName": error.name
    }), 404)

@app.errorhandler(500)
def handle_500_error(error):
    return make_response(jsonify({
        "errorCode": error.code,
        "errorDescription": "Internal Server Error",
        "errorDetailedDescription": error.description,
        "errorName": error.name
    }), 500)