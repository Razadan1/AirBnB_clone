#!/usr/bin/env python3
""" This module is the Base model class"""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """ This is the Base Model class which other classes will inherit from"""
    def __init__(self) -> None:
        self.id=str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self) -> None:
        self.updated_at = datetime.now()
    
    def to_dict(self) -> None:
        obj_json = self.__dict__
        obj_json['__class__'] = self.__class__.__name__
        obj_json['created_at'] = obj_json['created_at'].isoformat()
        obj_json['updated_at'] = obj_json['updated_at'].isoformat()
        return obj_json
    
model = BaseModel()
print(model)