# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

app = FastAPI()


# origins = [
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["*"],  
)

# Include the router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quality of Life Prediction API!"}
