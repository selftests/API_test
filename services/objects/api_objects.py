import allure
import requests

from utils.helper import Helper
from services.objects.endpoints import Endpoints
from services.objects.payloads import Payloads
#from config.headers import Headers
from services.objects.models.object_model import ObjectModel
#from conftest import obj_id

HOST = "https://api.restful-api.dev"

class ObjectsAPI(Helper):

    response: requests.Response
    
    
    def __init__(self):        
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        #self.headers = Headers()
        
    

    @allure.step("Create user")
    def create_object(self):
        response = requests.post(
            url=self.endpoints.create_add_object,
            #headers=self.headers.basic,
            json=self.payloads.create_add_object
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = (response.json())
        return model        
        
    
    @allure.step("Get users by ID")
    def get_object_by_id(self):
        response = requests.get(
            url=self.endpoints.get_object_by_id,
            #headers=self.headers.basic,            
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = (response.json())
        return model  
    
    

    @allure.step("Create object name")
    def create_object_name(self):       
        response = requests.post(
            url=self.endpoints.create_add_object,
            #headers=self.headers.basic,
            json=self.payloads.create_add_object
        )
        
        #print(response.status_code)
        print(self.payloads.create_add_object['name'])
        #print(response.json())
        #print(response.json()['name'])
        assert response.status_code == 200, response.json()
        assert response.json()['name'] == (self.payloads.create_add_object['name'])        
        self.attach_response(self.payloads.create_add_object['name'])
        model = (self.payloads.create_add_object['name'])
        return model

    
    @allure.step("Get obj_id")
    def get_object_obj_id(self, obj_id):
        
        #print(obj_id)
        response = requests.get(            
            url=f'{HOST}/objects/{obj_id}'
        )
        #print(response.json())
        #print(response.json()['id'])
        #print(obj_id)
        assert response.status_code == 200, response.json()       
        assert response.json()['id'] == obj_id
        self.attach_response(obj_id)
        model = (obj_id)
        return model

    

    @allure.step("Update obj_id")
    def update_object(self, obj_id):
        
        payload = Payloads.update_object        
        response = requests.put(
            url=f'{HOST}/objects/{obj_id}',
            json = self.payloads.update_object
        )
        #print(response.json())
        #print(response.json()['id'])
        #print(obj_id)
        assert response.status_code == 200, response.json()       
        assert response.json()['name'] == payload['name']
        self.attach_response(response.json()['name'])
        model = (response.json()['name'])
        return model
    

    @allure.step("Delete obj_id")
    def delete_object(self, obj_id):


        response = requests.delete(url=f'{HOST}/objects/{obj_id}')
        print(response.status_code) 
        assert response.status_code == 200, response.json()              
        response = requests.get(url=f'{HOST}/objects/{obj_id}')
        print(response.status_code)
        assert response.status_code == 404, response.json()
        self.attach_response(response.json())
        model = (response.json())
        return model
        