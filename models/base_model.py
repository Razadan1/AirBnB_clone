from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self) -> None:
        self.id=str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] (self.id) {self.__dict__}"
    
    def save(self) -> None:
        self.updated_at = datetime.now()
    
    def to_dict(self) -> None:
        to_json = self.__dict__
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = to_json['created_at'].isoformat()
        to_json['updated_at'] = to_json['updated_at'].isoformat()
        return to_json
    
model = BaseModel()
print(model)