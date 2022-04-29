from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message':'hoe'}


@app.get("/posts")
def get_things():
    return {'data':'yeah buddy'}