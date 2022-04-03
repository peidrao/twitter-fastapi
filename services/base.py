from typing import Any, Generic, List, Optional, Type, TypeVar
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import BaseModel

# from database.session import Base as BaseSession


# ModelType = TypeVar('ModelType', bound=BaseSession)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


# class Base(Generic[ModelType, CreateSchemaType]):
#     def __init__(self, model: Type[ModelType]):
#         self.model = model

#     def create(self, db: Session, request: CreateSchemaType) -> CreateSchemaType:
#         data = jsonable_encoder(request)
#         data_object = self.model(**data)
#         db.add(data_object)
#         db.commit()
#         db.refresh(data_object)
#         return data_object