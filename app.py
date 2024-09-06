# app.py
from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert data into numpy array for prediction
    features = np.array(data['features']).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return prediction result
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
