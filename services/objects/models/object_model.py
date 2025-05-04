from pydantic import BaseModel, field_validator


class ObjectModel(BaseModel):
   
    id: str
    name: str
    #data: str
    #year: str
    #price: str
    #CPU_model: str
    #Hard_disk_size: str
    uuid: str
    obj_id: str


    #@field_validator('name', 'year', 'price','CPU_model', 'Hard_disk_size', 'uuid')
    #def fields_are_not_empty(cls, value):
        #if value == "" or value is None:
        #    raise ValueError("Field is empty")
        #else:
        #return value



