from classes.meals import *
from classes.mealbox import MealBox
from classes.maindish import MainDishBuilder

mealbox = MainDishBuilder()

mealbox.make_meal()

print(mealbox._children)
print(mealbox.get_price())