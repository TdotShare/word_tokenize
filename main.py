from fastapi import FastAPI
from pythainlp.tokenize import word_tokenize
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


class ResponseData(BaseModel):
    text: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello TdotDev" , "api" : "FastAPI - Python"}


@app.post("/api/word_tokenize")
def tokenize(data: ResponseData):
    try:
        tokens = word_tokenize(
            text=data.text, engine="newmm", keep_whitespace=False)
        return {'status': 'success',
                'bypass': True,
                'data': unique(tokens)}
    except Exception as e:
        return {'status': 'error',
                'bypass': False,
                'message': 'Exception: ' + str(e)}


def unique(item):
    unique_list = []
    for x in item:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list
     