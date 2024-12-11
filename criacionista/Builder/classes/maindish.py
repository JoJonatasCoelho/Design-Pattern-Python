from classes.meals import *
from interfaces.meal_builder import MealCompositeBuilder
from classes.mealbox import MealBox

class MainDishBuilder(MealCompositeBuilder):
    _meal_box: MealBox

    def make_meal(self):
        arroz = Rice("John", 13)
        feijao = Beans("Feijoada", 10)
        carne  = Meat("Picanha", 40)

        self._meal_box.add([arroz, feijao, carne])

        return self._meal_box
    
    def get_meal(self):
        return self._meal_box