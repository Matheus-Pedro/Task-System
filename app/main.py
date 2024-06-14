# import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    test: int
    test2: str

@app.get("/")
async def test_hello() -> str:
    return {"Hello": "World"}


@app.post("/example")
async def text(testinp: Test) -> str:
    return testinp.test2

# if __name__ == "__main__":
#     uvicorn.run(app, port=9000)]
