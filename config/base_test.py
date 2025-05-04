from services.objects.api_objects import ObjectsAPI

class BaseTest:

    def setup_method(self):
        self.api_objects = ObjectsAPI()
