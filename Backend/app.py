from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
import logging
import pytz

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Error handling
try:
    client = MongoClient('localhost', 27017)
    db = client.flask_db
    todos = db.todos
    client.server_info()  # This will raise an exception if the connection fails
    app.logger.info("Connected to MongoDB successfully!")
except Exception as e:
    app.logger.error(f"Failed to connect to MongoDB. Error: {e}")

# Setup MongoDB connection
mongo_db_url = os.environ.get("MONGO_DB_CONN_STRING")
client = MongoClient(mongo_db_url)
db = client['sensors_db']
collection = db['sensors']

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Sensors API",
        "endpoints": {
            "GET/POST": "/api/sensors",
            "PUT/DELETE": "/api/sensors/<id>"
        }
    })

@app.route("/api/sensors", methods=['GET', 'POST'])
def handle_sensors():
    if request.method == 'POST':
        sensor_data = request.json
        #Insert current time
        cst = pytz.timezone('US/Central')
        sensor_data['timestamp'] = datetime.now(cst)
        
        # Insert the data into MongoDB
        result = collection.insert_one(sensor_data)
        
        return jsonify({"message": "Sensor data added successfully", "id": str(result.inserted_id)}), 201
    
    elif request.method == 'GET':
        sensor_id = request.args.get('sensor_id')
        filter = {} if sensor_id is None else {"sensor_id": sensor_id}
        sensors = list(collection.find(filter))
        
        # Convert ObjectId to string for JSON serialization
        for sensor in sensors:
            sensor['_id'] = str(sensor['_id'])
        
        return jsonify(sensors), 200

@app.route("/api/sensors/<id>", methods=['PUT', 'DELETE'])
def handle_sensor(id):
    if request.method == 'PUT':
        update_data = request.json
        result = collection.update_one({'_id': ObjectId(id)}, {"$set": update_data})
        if result.modified_count == 0:
            return jsonify({"error": "Sensor not found"}), 404
        return jsonify({"message": "Sensor updated successfully"}), 200
    
    elif request.method == 'DELETE':
        result = collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Sensor not found"}), 404
        return jsonify({"message": "Sensor deleted successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)