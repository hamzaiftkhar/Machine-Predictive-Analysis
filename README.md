
# Machine Predictive Maintenance Analysis

This project is a web application for predicting machine failure types using a Random Forest model. The application processes various input features related to machine operations and predicts potential failures. The web app is built using Flask and includes preprocessing steps for feature engineering and transformation.

## Features

The application predicts the following failure types:
- No Failure
- Power Failure
- Tool Wear Failure
- Overstrain Failure
- Random Failures
- Heat Dissipation Failure

## Dataset Features

- **Type:** Machine type (M, L, H)
- **Air temperature [K]:** Air temperature in Kelvin
- **Process temperature [K]:** Process temperature in Kelvin
- **Rotational speed [rpm]:** Rotational speed in RPM
- **Torque [Nm]:** Torque in Nm
- **Tool wear [min]:** Tool wear in minutes
- **Target:** Actual failure type
- **Temperature difference [°C]:** Calculated as the difference between process and air temperatures

## Preprocessing

1. **Encoding Categorical Variables:** The `Type` feature is converted to numeric using a mapping: {'M': 1, 'L': 2, 'H': 3}.
2. **Temperature Conversion:** Temperatures are converted from Kelvin to Celsius.
3. **Feature Engineering:** Additional feature for temperature difference is calculated.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- NumPy
- scikit-learn
- Joblib
- Pickle

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/machine-predictive-maintenance.git
   cd machine-predictive-maintenance
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Load the model and encoder:**

   Ensure you have the model and encoder files in the `model/` directory:

   - `random_forest_model.pkl`
   - `ordinal_encoder.joblib` (if used)

### Running the Application

1. **Start the Flask application:**

   ```bash
   python app.py
   ```

2. **Open your browser and go to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Enter the required features and submit the form to get a prediction.**

## File Structure

- `app.py`: Main application file
- `templates/`: HTML templates for rendering web pages
  - `index.html`: Main input form page
  - `result.html`: Result display page
- `model/`: Directory containing the model and encoder files

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add a new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request


## Contact

For questions or suggestions, please contact hamzaiftikhar135@gmail.com.

