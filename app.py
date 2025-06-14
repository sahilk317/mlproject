import numpy as np
import pandas as pd
from fastapi import FastAPI,Request
from pydantic import BaseModel,Field
from typing import Annotated ,Literal
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class StudentPerformence(BaseModel):
    
    gender: Annotated[Literal['male', 'female'], Field(...)]
    race_ethnicity: Annotated[
        Literal['group A', 'group B', 'group C', 'group D', 'group E'],
        Field(...)
    ]
    parental_level_of_education: Annotated[
        Literal[
            "some college", "associate's degree", "high school",
            "some high school", "bachelor's degree", "master's degree"
        ],
        Field(...)
    ]
    lunch: Annotated[Literal['standard', 'free/reduced'], Field(...)]
    test_preparation_course: Annotated[Literal['none', 'completed'], Field(...)]
    reading_score: Annotated[int, Field(..., ge=0, le=100)]
    writing_score: Annotated[int, Field(..., ge=0, le=100)]



@app.get('/',response_class=HTMLResponse)
@app.get('/home',response_class=HTMLResponse)
async def get_form(request:Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.post('/predict')
async def predict(student_performence : StudentPerformence):
    data = CustomData(
        student_performence.gender,
        student_performence.race_ethnicity,
        student_performence.parental_level_of_education,
        student_performence.lunch,
        student_performence.test_preparation_course,
        student_performence.reading_score,
        student_performence.writing_score
    )

    input_df = data.get_data_as_data_frame()
    print(input_df)

    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(input_df)


    return {"result": float(prediction[0])}









