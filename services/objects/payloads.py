#from faker import Faker

#fake = Faker()

class Payloads:

        
    create_add_object = {
      "name": "Apple MacBook Pro 16",
      "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
        }
    }

    update_object = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 2049.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }   