# ECG based Emotion_classification
This project is a real-time ECG Emotion Detection System that uses an Arduino UNO and AD8232 ECG sensor to capture heart signals, processes them using an LSTM-based deep learning model, and displays the heart rate and predicted emotional state through a web interface.

**TECH STACK USED**
  - Frontend: React.js
  - Backend: Flask (Python)
  - Machine Learning: LSTM model (Keras)
  - Cloud Platform: ThingSpeak (for ECG data logging)
  - Hardware: Arduino UNO, AD8232 ECG Sensor, 3 Lead ECG wire, Jumper wires, Disposable ECG Electrodes, USB-A Male to B Male Cable

**SYSTEM OVERVIEW**
1. Process Flow
   - ECG Sensor captures raw electrical signals from the body.
   - Arduino UNO reads the ECG data and transmits it.
   - LSTM-based ML Model classifies the user's emotional state from ECG input.
   - Output :
     - Displayed in a web interface (heartbeat + emotion)
     - Sent to ThingSpeak for logging and future analysis

2. Hardware Setup
   - Electrodes are attached at RA, LA, and RL positions on the body.
   - AD8232 filters and amplifies the ECG signals.
   - Arduino UNO transmits the processed signals to the ML model via USB.
   - Data is analyzed, visualized, and stored in real-time.



