import allure
import pytest

from config.base_test import BaseTest



@allure.epic("Administration")
@allure.feature("Objects")
class TestObjects(BaseTest):

    @pytest.mark.users
    @allure.title("Create new object")
    def test_create_object(self):
        user = self.api_objects.create_object()
        print(user)        
        #self.api_users.get_user_by_id()        

    @pytest.mark.users
    @allure.title("Get object")
    def test_get_object(self):
        self.api_objects.get_object_by_id()
        print(self.api_objects.get_object_by_id())

    
    @pytest.mark.object
    @allure.title("Create new object name")
    def test_create_object_name(self):
        self.api_objects.create_object_name()
        print(self.api_objects.create_object_name())

    
    
    @pytest.mark.object
    @allure.title("Get obj_id")
    def test_get_object_id(self, obj_id):
        self.api_objects.get_object_obj_id(obj_id)
        print(self.api_objects.get_object_obj_id(obj_id))

    @pytest.mark.object
    @allure.title("Put new obj_id")
    def test_update_object(self, obj_id):
        self.api_objects.update_object(obj_id)
        print(self.api_objects.update_object(obj_id))
    
    @pytest.mark.object
    @allure.title("Delete obj_id")
    def test_delete_object(self, obj_id):
        self.api_objects.delete_object(obj_id)
        print(self.api_objects.delete_object(obj_id))
        





    
    
    
    
   