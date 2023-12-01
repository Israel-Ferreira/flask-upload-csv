import json

class Product:

    def __init__(self, sku, model, manufacturer,price):
        self.__sku = sku
        self.model = model
        self.__manufacturer = manufacturer
        self.__price =  price


    @property
    def sku(self):
        return self.__sku
    

    @property
    def manufacturer(self):
        return self.__manufacturer
        

    def apply_discount(self, discount_percentage_value):
        percentage_float_val =  discount_percentage_value / 100

        discount_value = self.__price * percentage_float_val

        self.__price -= discount_value


    def to_dict(self):
        return  {
            "sku": self.__sku,
            "model": self.model,
            "manufacturer": self.__manufacturer,
            "price": self.__price,
        }
    

    def __str__(self):
        product_dict =  self.to_dict()
        return json.dumps(product_dict)

    
