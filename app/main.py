import uvicorn
from controller.controller import app

async def main():
    uvicorn.run(app, port=8000)

if __name__ == "__main__":
    main()
