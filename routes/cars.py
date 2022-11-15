from fastapi import APIRouter, Response, status
from config.db import mongo
from schemas.car_schema import car_entity, cars_entity
from models.car_model import CarModel
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

car = APIRouter()  # instance that contain paths for http methods


@car.get('/cars', response_model=list[CarModel], tags=["cars"])
def find_all_cars():
    return cars_entity(mongo.cars_db.cars.find())


@car.post('/cars', response_model=CarModel, tags=["cars"])
def create_car(car: CarModel):  # here we received body or the "response"
    new_car = dict(car)  # "car" contains all fields of the model
    del new_car["id"]  # we deleted id, because mongo assigns it by default
    id = mongo.cars_db.cars.insert_one(new_car).inserted_id  # here we inserted new car object with its id
    car = mongo.cars_db.cars.find_one({"_id": id}) # return the car object 
    return car_entity(car) # we pass car object in our car entity to give it formatting


@car.get('/cars/{id}', response_model=CarModel, tags=["cars"])
def find_car(id: str):
    return car_entity(mongo.cars_db.cars.find_one({"_id": ObjectId(id)}))


@car.put('/cars/{id}', response_model=CarModel, tags=["cars"])
def update_car(id: str, car: CarModel):
    mongo.cars_db.cars.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(car)})
    return car_entity(mongo.cars_db.cars.find_one({"_id": ObjectId(id)}))


@car.delete('/cars/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["cars"])
def delete_car(id: str):
    car_entity(mongo.cars_db.cars.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
