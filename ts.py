import serial
import requests
import time

# ThingSpeak API details
THINGSPEAK_WRITE_API_KEY = "L3D8H0AW3UT7OI53"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Open serial connection to Arduino (check COM port)
ser = serial.Serial('COM3', 9600, timeout=1)  
time.sleep(2)  # Allow time for connection setup

def send_to_thingspeak(ecg_value):
    """Send ECG data to ThingSpeak"""
    payload = {
        "api_key": "L3D8H0AW3UT7OI53",
        "field1": ecg_value
    }
    response = requests.get(THINGSPEAK_URL, params=payload)
    print(f"Sent {ecg_value} to ThingSpeak. Response: {response.text}")

try:
    while True:
        if ser.in_waiting > 0:
            raw_data = ser.readline().decode('utf-8', errors='ignore').strip()  # Read ECG data
            print(f"Received from Arduino: {raw_data}")  # Debugging output

            if raw_data.isdigit():  # Ensure it's a valid number
                send_to_thingspeak(raw_data)
                time.sleep(15)  # ThingSpeak allows updates every 15 sec

except KeyboardInterrupt:
    print("\nStopping data transmission")
    ser.close()  # Close serial connection
