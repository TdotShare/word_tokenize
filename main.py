from fastapi import FastAPI
from pythainlp.tokenize import word_tokenize
import uvicorn

from pydantic import BaseModel


class ResponseData(BaseModel):
    text: str


app = FastAPI()


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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)


def unique(item):
    unique_list = []
    for x in item:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list
     