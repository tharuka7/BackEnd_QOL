# app/models.py
from typing import List

from pydantic import BaseModel


class QualityOfLifeInput(BaseModel):
    familiarity_with_ethnic_origin: int
    smoke_detector: int
    airport: int
    full_time_employment: int
    access_to_a_computer: int
    student: int
    parks_and_recs: int
    city_effort_satisfaction: int
    nursing_home: int
    ethnicity: int
    public_safety: int
    libraries: int
    home_phone: int
    mobile_devices: int
