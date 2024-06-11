import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# Load the model (ensure the path is correct)
model = pickle.load(open('C:/Users/victuds/Desktop/Intern project/flask/Random_model.pkl', 'rb'))



@app.route('/')
def home():
    # Render the template from the specified path
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        lead_time = int(request.form['lead_time'])
        average_price = float(request.form['average_price'])
        special_requests = int(request.form['special_requests'])
        month = int(request.form['Month'])
        day_of_week = int(request.form['Day_of_week'])
        days_of_reservation = int(request.form['Days_of_reservation'])
        market_segment_type_online = int(request.form['market_segment_type_Online'])
        
        # Preprocess input data
        features = preprocess_input(lead_time, average_price, special_requests, month, day_of_week, days_of_reservation, market_segment_type_online)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return prediction result
        result = 'Booking should be canceled' if prediction == 1 else 'Booking should not be canceled'
        return render_template('result.html', result=result)
    except Exception as e:
        # Log the exception (you might want to use logging module for a real-world application)
        print(e)
        return render_template('error.html')


def preprocess_input(lead_time, average_price, special_requests, month, day_of_week, days_of_reservation, market_segment_type_online):
    features = np.array([lead_time, average_price, special_requests, month, day_of_week, days_of_reservation, market_segment_type_online]).reshape(1, -1)
    return features

if __name__ == '__main__':
    app.run(debug=True)
