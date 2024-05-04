import uvicorn
from fastapi import FastAPI

from src.database import engine, Base
from src.measurements.router import router as measurements_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(measurements_router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8005)
