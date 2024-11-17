
# This file is set up to be mainly focused with connecting the backend (api included ) and the frontend.
from flask import Flask, jsonify
from pymongo import MongoClient
from MLModel import get_ideal_temperature, get_ideal_humidity, get_ideal_sunlight

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sensors_db"]
collection = db["sensors"]

@app.route('/api/sensor_data', methods=['GET'])
def get_sensor_data():
    sensor_data_cursor = collection.find()
    sensor_data_list = list(sensor_data_cursor)
    return jsonify(sensor_data_list)

@app.route('/api/ideal_conditions', methods=['GET'])
def get_ideal_conditions():
    ideal_conditions = {
        "temperature": get_ideal_temperature(),
        "humidity": get_ideal_humidity(),
        "sunlight": get_ideal_sunlight()
    }
    return jsonify(ideal_conditions)

if __name__ == '__main__':
    app.run(debug=True)