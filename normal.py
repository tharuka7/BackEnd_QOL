import pandas as pd
import pickle

# Load the model from the pkl file
with open('rf_classifier_top.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the function to predict the 'Quality of Life'
def predict_quality_of_life(input_data):
    # Corrected feature names (matching those during model training)
    feature_names = [
        'Satisfied With Life 1', 'Satisfied With Life 2', 'Present Mental Health',
        'English Speaking', 'Income', 'Present Health', 'Satisfaction With Housing.',  # with period
        'Present Oral Health', 'Language', 'Interpretation (Medical)',
        'Comunication Problem',  # misspelled in training data
        'Achieving Ends Meet', 'Familiarity with America',
        'English Difficulties', 'Ethnicity', 'Small Businesses ',  # with extra space
        'Religious Attendance', 'Parks and Recs', 'Place to Work', 'Airport'
    ]

    # Convert the input data into a DataFrame with matching feature names
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Check if feature names match
    if set(feature_names) != set(model.feature_names_in_):
        print("Feature name mismatch. Please check the input data.")
        print("Input feature names:", input_df.columns.tolist())
        return None

    # Predict the quality of life
    prediction = model.predict(input_df)

    # Map the prediction to the corresponding quality of life
    quality_of_life_mapping = {0: 'Good', 1: 'Moderate', 2: 'Poor'}
    return quality_of_life_mapping[prediction[0]]

# Example usage
sample_input_array = [
    1,  # Satisfied With Life 1: Disagree
    0,  # Satisfied With Life 2: Agree
    2,  # Present Mental Health: Good
    2,  # English Speaking: Very well
    3,  # Income: $30,000 - $39,999
    2,  # Present Health: Good
    3,  # Satisfaction With Housing: Very much
    0,  # Present Oral Health: Excellent
    3,  # Language: English
    0,  # Interpretation (Medical): No
    0,  # Communication Problem: No
    1,  # Achieving Ends Meet: Yes
    1,  # Familiarity with America: Low
    1,  # English Difficulties: Not at all
    0,  # Ethnicity: Asian Indian
    2,  # Small Businesses: Good
    2,  # Religious Attendance: Once or twice a month
    3,  # Parks and Recs: Pretty much satisfied
    2,  # Place to Work: Good
    0   # Airport: Never used
]

# Print the prediction
print(predict_quality_of_life(sample_input_array))
