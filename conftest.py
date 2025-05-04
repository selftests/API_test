#import os
#from dotenv import load_dotenv
import requests
import pytest
from services.objects.payloads import Payloads
#load_dotenv()

HOST = "https://api.restful-api.dev" 


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.get(
        url=f"{HOST}/objects"
        #headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    print(response.status_code)
    assert response.status_code == 200
    
@pytest.fixture(autouse=True, scope="session")
def obj_id():
    payload = Payloads.create_add_object
    respons = requests.post(url=f"{HOST}/objects",json = payload).json()
    yield respons['id']
    requests.delete(f'{HOST}/objects/{respons["id"]}')
