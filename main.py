from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from routes.cars import car

app = FastAPI(
    title='Cars API with FastAPI and MongoDb',
    description='This is a simple REST API using fastapi and mongodb',
    version='0.0.1',
)
app.include_router(car)

origins = [
    
    "http://10.0.2.2", # for android emulator
    "http://127.0.0.1",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True, host='0.0.0.0') # we launch server in 0.0.0.0:8000 for testing in real device
    #uvicorn.run("main:app", port=8000, reload=True)