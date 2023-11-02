from tokenize import String
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title = 'Sepsis Prediction')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9000" ],  # Lista de dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Cabeceras permitidas (puedes especificar las necesarias)
)

model = load(pathlib.Path('model/sepsis.joblib'))

class InputData(BaseModel):
    age_years:int=21
    sex_0male_1female:int=1
    episode_number:int=1
 
   
    
class OutputData(BaseModel):
    score:float=0.80318881046519

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict_proba(model_input)[:,-1]

    return {'score':result}

