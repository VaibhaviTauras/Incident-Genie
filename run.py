import uvicorn
from config.config import settings

from fastapi import FastAPI, HTTPException


app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=settings.DEBUG)
