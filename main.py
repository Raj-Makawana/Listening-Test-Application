from fastapi import FastAPI, Query, HTTPException, status, Path
from fastapi.responses import JSONResponse
from models import Name_score, New_Test_Taker, NameScoreResponse, TestScoreResponse
from mongoengine import connect
from typing import List
import json
import pymongo
import mongoengine

app = FastAPI()

# Connect to mongoDB using mongoengine
connect(db="ListeningAppDB", host="localhost", port=27017)
collection_name = "name_score"

@app.get("/")
def home_page():
    return {"message": "Welcome to the home page"}

from fastapi import HTTPException, status

@app.post("/score", response_model=TestScoreResponse)
def new_test_taker(test_taker: New_Test_Taker):
    new_test_taker = Name_score(
        name=test_taker.name,
        score=test_taker.score
    )
    new_test_taker.save()

    # Create a response with both the message and details
    response = TestScoreResponse(
        message="Test score has been recorded successfully",
        details=NameScoreResponse(
            name=new_test_taker.name,
            score=new_test_taker.score
        )
    )

    return response

@app.get("/score")
def get_score():
    test_takers = Name_score.objects()

    test_taker_list = [{
        "name": test_taker.name,
        "score": test_taker.score
    } 
    for test_taker in test_takers
    ]

    return {"Test taker's Scores": test_taker_list}

from typing import List

@app.get("/search-name")
def search_name(name: str, score: int = Query(None, gt=0)):
    test_takers = Name_score.objects.filter(name__icontains=name)
    test_taker_list = []

    for test_taker in test_takers:
        test_taker_dict = {
            "name": test_taker.name,
            "score": test_taker.score
        }
        test_taker_list.append(test_taker_dict)

    return {"Test takers": test_taker_list}

@app.get("/search-score")
def search_score(score: int = Query(None, gt=0)):
    test_takers = Name_score.objects(score=score)
    test_taker_list = []

    for test_taker in test_takers:
        test_taker_dict = {
            "name": test_taker.name,
            "score": test_taker.score
        }
        test_taker_list.append(test_taker_dict)

    return {"Test takers with Score": test_taker_list}