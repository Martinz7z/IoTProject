from flask import Flask, render_template, jsonify
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB setup
def setup_mongodb():
    client = MongoClient('put client key here')

    db = client['put the db name here']
    return db['put collection name here']

# Function to fetch last entries from MongoDB
def fetch_last_entries(collection, count=20):
    entries = list(collection.find().sort('timestamp', -1).limit(count))
    return entries

# Function to store data in MongoDB
def push_to_mongodb(temperature, humidity, timestamp):
    collection = setup_mongodb()
    collection.insert_one({
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': timestamp
    })

# PubNub configuration
pnconfig = PNConfiguration()
pnconfig.publish_key = 'put your key here'
pnconfig.subscribe_key = 'put your key here'
pnconfig.uuid = 'put the uuid here'
pubnub = PubNub(pnconfig)

# Data storage
data_list = fetch_last_entries(setup_mongodb(), count=20)

class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        data = message.message
        temperature = data.get('temperature', None)
        humidity = data.get('humidity', None)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        data_list.append({'temperature': temperature, 'humidity': humidity, 'timestamp': timestamp})
        if len(data_list) > 100:
            data_list.pop(0)
        
        push_to_mongodb(temperature, humidity, timestamp)

# Add the listener
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('put your channel here').execute()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    timestamps = [entry['timestamp'] for entry in data_list]
    temperatures = [entry['temperature'] for entry in data_list]
    humidities = [entry['humidity'] for entry in data_list]

    return jsonify({
        'timestamps': timestamps,
        'temperatures': temperatures,
        'humidities': humidities
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
