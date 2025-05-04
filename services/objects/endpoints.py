#import os
import conftest

HOST = "https://api.restful-api.dev" 



class Endpoints():

    create_add_object = f"{HOST}/objects"
    #get_object_by_id_1 = lambda self, uuid: f"{HOST}/objects/{uuid}"
    #get_object_obj_id = (f'{HOST}/objects/{obj_id}')
    get_object_by_id =  f"{HOST}/objects/7"
