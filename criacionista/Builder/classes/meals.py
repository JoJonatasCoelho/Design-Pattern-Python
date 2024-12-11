# preguica de ficar criando classe por classe em arquivo
from interfaces.meal import MealComposite

class Rice(MealComposite):
    
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price


class Beans(MealComposite):
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price


# class Rice(MealComposite):
#     def __init__(self, name, price):
#         self.name = name
#         self._price = price

#     def get_price(self):
#         return self._price


class Meat(MealComposite):
    def __init__(self, name, price):
        self.name = name
        self._price = price     

    def get_price(self):
        return self._price
    