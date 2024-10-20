# app/models.py
from pydantic import BaseModel
from typing import List

class QualityOfLifeInput(BaseModel):
    satisfied_with_life_1: int
    satisfied_with_life_2: int
    present_mental_health: int
    english_speaking: int
    income: int
    present_health: int
    satisfaction_with_housing: int
    present_oral_health: int
    language: int
    interpretation_medical: int
    communication_problem: int
    achieving_ends_meet: int
    familiarity_with_america: int
    english_difficulties: int
    ethnicity: int
    small_businesses: int
    religious_attendance: int
    parks_and_recs: int
    place_to_work: int
    airport: int

