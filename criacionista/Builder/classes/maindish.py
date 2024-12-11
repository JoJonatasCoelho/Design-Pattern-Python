from interfaces.meal_builder import MealCompositeBuilder
from classes.mealbox import MealBox

class MainDishBuilder(MealCompositeBuilder):
    _meal_box: MealBox