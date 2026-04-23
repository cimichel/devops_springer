from fastapi import FastAPI
import random
from springer.pipeline import apply

app = FastAPI(
    title="🎭 DevOps Springer API",
    description="""
## Welcome to chaos engineering with feelings

This API simulates:

- 💥 Broken pipelines  
- 🎤 Audience reactions  
- 🤡 Developer excuses  

Because production is basically live TV.
""",
    version="1.0.0"
)

JERRY_LINES = [
    "So you said this was production-ready… that was a lie.",
    "You deployed on a Friday? Interesting choice.",
    "This pipeline is out of control.",
]

AUDIENCE = [
    "JERRY! JERRY! JERRY!",
    "BOOOOOOOO",
    "*throws chair*",
]


@app.get("/")
def root():
    return {"message": "DevOps Springer API is running 🎭"}


@app.get("/jerry", tags=["🎭 Jerry"])
def get_jerry():
    return {"quote": random.choice(JERRY_LINES)}


@app.get("/audience", tags=["🎤 Audience"])
def get_audience():
    return {"reaction": random.choice(AUDIENCE)}


@app.post("/pipeline/run", tags=["💥 Pipeline"])
def run_pipeline():
    apply()
    return {"status": "Pipeline executed 🎭"}
