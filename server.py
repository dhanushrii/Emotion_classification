from flask import Flask, jsonify
from flask_cors import CORS
import requests
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained ECG emotion model
model = load_model("ecg_emotion_model.h5")

# StandardScaler to normalize heart rate values
scaler = StandardScaler()
scaler.mean_ = np.array([85])  # Adjust based on your training dataset mean
scaler.scale_ = np.array([15])  # Adjust based on your training dataset std dev

# ThingSpeak Channel Information
THING_SPEAK_CHANNEL_ID = "2869939"  # Your ThingSpeak Channel ID
THING_SPEAK_API_KEY = "OUCCLWOZ3P8FHBG7"  # Your ThingSpeak API Key
THING_SPEAK_URL = f"https://api.thingspeak.com/channels/{THING_SPEAK_CHANNEL_ID}/fields/1.json?api_key={THING_SPEAK_API_KEY}&results=1"

# Function to fetch heart rate from ThingSpeak
def fetch_heart_rate():
    response = requests.get(THING_SPEAK_URL)
    if response.status_code == 200:
        data = response.json()
        feeds = data.get("feeds", [])
        if feeds and feeds[0]["field1"]:
            try:
                heart_rate = float(feeds[0]["field1"])  # Get latest heart rate value
                return heart_rate
            except ValueError:
                return None  # Handle invalid data
    return None  # Return None if data is unavailable

# Function to predict emotion based on heart rate
def predict_emotion(heart_rate):
    heart_rate_scaled = scaler.transform([[heart_rate]])  # Normalize data
    prediction = model.predict(heart_rate_scaled)
    predicted_class = np.argmax(prediction)

    # Adjust labels based on your trained model classes
    emotion_labels = ["happy", "sad", "angry", "neutral", "fear"]
    return emotion_labels[predicted_class]

# API Route to get emotion prediction
@app.route('/get_emotion', methods=['GET'])
def get_emotion():
    heart_rate = fetch_heart_rate()
    if heart_rate is None:
        return jsonify({"error": "Failed to fetch heart rate"}), 500

    emotion = predict_emotion(heart_rate)
    return jsonify({"heart_rate": heart_rate, "emotion": emotion})

# Add a simple home route to check server status
@app.route('/')
def home():
    return "Flask server is running!"

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
