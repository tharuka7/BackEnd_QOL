# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()


origins = [
    "https://black-river-065d1510f.5.azurestaticapps.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quality of Life Prediction API!"}
