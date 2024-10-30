# app/services.py
import pickle

import pandas as pd

# Load the model from the pkl file (only once to avoid reloading in each request)
with open('stacking_clf.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the function to predict the 'Quality of Life'
def predict_quality_of_life(input_data):
    feature_names = [
        'Familiarity with Ethnic Origin', 'Smoke Detector', 'Airport',
        'Full Time Employment', 'Access to a Computer', 'Student', 
        'Parks and Recs', 'City Effort Satisfaction', 'Nursing Home', 
        'Ethnicity', 'Public Safety', 'Libraries', 'Home Phone', 'Mobile Devices'
    ]

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Check for feature mismatch
    if set(feature_names) != set(model.feature_names_in_):
        return "Feature name mismatch. Please check the input data."

    # Predict using the model
    prediction = model.predict(input_df)

    # Map the prediction to quality of life
    quality_of_life_mapping = {0: 'Poor', 1: 'Moderate', 2: 'Good'}
    return quality_of_life_mapping[prediction[0]]
