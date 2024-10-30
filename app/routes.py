# app/routes.py
from fastapi import APIRouter

from app.models import QualityOfLifeInput
from app.services import predict_quality_of_life

router = APIRouter()

@router.post("/predict/")
def predict(input_data: QualityOfLifeInput):
    # Convert input data from Pydantic model to list format
    input_data_list = [
        input_data.familiarity_with_ethnic_origin,
        input_data.smoke_detector,
        input_data.airport,
        input_data.full_time_employment,
        input_data.access_to_a_computer,
        input_data.student,
        input_data.parks_and_recs,
        input_data.city_effort_satisfaction,
        input_data.nursing_home,
        input_data.ethnicity,
        input_data.public_safety,
        input_data.libraries,
        input_data.home_phone,
        input_data.mobile_devices
    ]

    # Call the prediction function
    prediction = predict_quality_of_life(input_data_list)

    return {"Quality of Life Prediction": prediction}
