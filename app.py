from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import joblib
import pickle
#import category_encoders as ce


app = Flask(__name__)

# Load the model and encoder
with open('model/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
#encoder = joblib.load('model/ordinal_encoder.joblib')

output_categories = {
    0: "No Failure",
    1: "Power Failure",
    2: "Tool Wear Failure",
    3: "Overstrain Failure",
    4: "Random Failures",
    5: "Heat Dissipation Failure"
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    data = request.form.to_dict()
    type_map = {'M': 1, 'L': 2, 'H': 3}
    data['Type'] = type_map[data['Type']]
    
    # Convert temperatures from K to °C
    data['Air temperature [K]'] = float(data['Air temperature [K]']) - 272.15
    data['Process temperature [K]'] = float(data['Process temperature [K]']) - 272.15
    data['Temperature difference [°C]'] = data['Process temperature [K]'] - data['Air temperature [K]']
    
    # Prepare features for the model
    features = [
        data['Type'],
        data['Air temperature [K]'],
        data['Process temperature [K]'],
        data['Rotational speed [rpm]'],
        data['Torque [Nm]'],
        data['Tool wear [min]'],
        data['Target'],
        data['Temperature difference [°C]']
    ]
    features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    output_category = output_categories[prediction[0]]
    #output = encoder.inverse_transform(prediction.reshape(-1, 1))[0][0]
    
    
    return render_template('result.html', prediction_text=f'Predicted Failure Type: {output_category}')

if __name__ == "__main__":
    app.run(debug=True)
