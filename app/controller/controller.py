from fastapi import FastAPI
from model.task import Task

app = FastAPI()

@app.get("/")
async def test_hello() -> dict:
    """Olá Mundo"""
    return {"Hello": "World"}

# @app.post("/example")
# async def text(testinp: Test) -> str:
#     return testinp.test2
