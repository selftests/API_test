import requests
import pytest
from services.objects.payloads import Payloads


def test_create_object():
    
    payload = Payloads.create_add_object
    respons = requests.post('https://api.restful-api.dev/objects', json = payload).json()
    print(payload['name'])
    assert respons['name'] == payload['name']
   

def test_get_object(obj_id):
    
    print(obj_id)
    respons = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert respons['id'] == obj_id



def test_update_object(obj_id):
    
    payload = Payloads.update_object
    respons = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json = payload).json()
    assert respons['name'] == payload['name']
   



def test_delete_object(obj_id):
    #obj_id = create_object()
    respons = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert respons.status_code == 200
    respons = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert respons.status_code == 404



#respons = requests.get(f'https://api.restful-api.dev/objects/ff808181932badb60194b1ec01131583').json()
#print(respons)
#Перепроверяем. что объект удалился. or POSTMAN.
#pytest -s -v