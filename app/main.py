from fastapi import FastAPI
from random import choice
from app.database import Base, engine
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

success_flow = [
    "Registration Request",
    "Authentication Request",
    "Authentication Response",
    "Security Mode Command",
    "Security Mode Complete",
    "Registration Accept"
]

failure_flow = [
    "Registration Request",
    "Authentication Request",
    "Authentication Failure",
    "Registration Reject"
]

@app.get("/")
def root():
    return {
        "project": "Cloud Native Telecom Operations Lab",
        "status": "running"
    }

@app.get("/attach")
def attach():
    return {
        "status": "success",
        "flow": success_flow
    }

@app.get("/attach/failure")
def attach_failure():
    return {
        "status": "failure",
        "flow": failure_flow
    }
attach_history = []

@app.get("/attach/store")
def store_attach():

    attach_history.append(
        {
            "result": "success"
        }
    )

    return {
        "count": len(attach_history)
    }


@app.get("/history")
def history():
    return attach_history