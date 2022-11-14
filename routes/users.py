from fastapi import APIRouter, Response, status
from config.db import mongo
from schemas.user_schema import user_entity, users_entity
from models.user_model import UserModel
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()  # instance that contain paths for http methods


@user.get('/users', response_model=list[UserModel], tags=["users"])
def find_all_user():
    return users_entity(mongo.local.user.find())


@user.post('/users', response_model=UserModel, tags=["users"])
def create_user(user: UserModel):  # here we received body or the "response"
    new_user = dict(user)  # "user" contains all fields of the model
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = mongo.local.user.insert_one(new_user).inserted_id
    user = mongo.local.user.find_one({"_id": id})
    return user_entity(user)


@user.get('/users/{id}', response_model=UserModel, tags=["users"])
def find_user(id: str):
    return user_entity(mongo.local.user.find_one({"_id": ObjectId(id)}))


@user.put('/users/{id}', response_model=UserModel, tags=["users"])
def update_user(id: str, user: UserModel):
    mongo.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return user_entity(mongo.local.user.find_one({"_id": ObjectId(id)}))


@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    user_entity(mongo.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
