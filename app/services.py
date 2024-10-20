# app/services.py
import pandas as pd
import pickle

# Load the model from the pkl file (only once to avoid reloading in each request)
with open('rf_classifier_top.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the function to predict the 'Quality of Life'
def predict_quality_of_life(input_data):
    feature_names = [
        'Satisfied With Life 1', 'Satisfied With Life 2', 'Present Mental Health',
        'English Speaking', 'Income', 'Present Health', 'Satisfaction With Housing.',
        'Present Oral Health', 'Language', 'Interpretation (Medical)',
        'Comunication Problem', 'Achieving Ends Meet', 'Familiarity with America',
        'English Difficulties', 'Ethnicity', 'Small Businesses ', 
        'Religious Attendance', 'Parks and Recs', 'Place to Work', 'Airport'
    ]

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Check for feature mismatch
    if set(feature_names) != set(model.feature_names_in_):
        return "Feature name mismatch. Please check the input data."

    # Predict using the model
    prediction = model.predict(input_df)

    # Map the prediction to quality of life
    quality_of_life_mapping = {0: 'Good', 1: 'Moderate', 2: 'Poor'}
    return quality_of_life_mapping[prediction[0]]
