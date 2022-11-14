from fastapi import FastAPI
import uvicorn
from routes.users import user

app = FastAPI(
    title='REST API with FastAPI and MongoDb',
    description='This is a simple REST API using fastapi and mongodb',
    version='0.0.1',
)
app.include_router(user)



if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)