# app/routes.py
from fastapi import APIRouter
from app.models import QualityOfLifeInput
from app.services import predict_quality_of_life

router = APIRouter()

@router.post("/predict/")
def predict(input_data: QualityOfLifeInput):
    # Convert input data from Pydantic model to list format
    input_data_list = [
        input_data.satisfied_with_life_1,
        input_data.satisfied_with_life_2,
        input_data.present_mental_health,
        input_data.english_speaking,
        input_data.income,
        input_data.present_health,
        input_data.satisfaction_with_housing,
        input_data.present_oral_health,
        input_data.language,
        input_data.interpretation_medical,
        input_data.communication_problem,
        input_data.achieving_ends_meet,
        input_data.familiarity_with_america,
        input_data.english_difficulties,
        input_data.ethnicity,
        input_data.small_businesses,
        input_data.religious_attendance,
        input_data.parks_and_recs,
        input_data.place_to_work,
        input_data.airport
    ]

    # Call the prediction function
    prediction = predict_quality_of_life(input_data_list)

    return {"Quality of Life Prediction": prediction}
