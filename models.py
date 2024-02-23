from mongoengine import Document, StringField, IntField
from pydantic import BaseModel

class Name_score(Document):
    name = StringField(required=True)
    score = IntField(required=True)

    def save(self, *args, **kwargs):
        super(Name_score, self).save(*args, **kwargs)

class New_Test_Taker(BaseModel):
    name: str
    score: int

class NameScoreResponse(BaseModel):
    name: str
    score: int

class TestScoreResponse(BaseModel):
    message: str
    details: NameScoreResponse
