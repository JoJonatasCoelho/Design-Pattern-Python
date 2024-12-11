from classes.meals import *
from classes.mealbox import MealBox

arroz = Rice("John", 13)
feijao = Beans("Feijoada", 10)
carne  = Meat("Picanha", 40)

box = [arroz, feijao, carne]

mealbox = MealBox()

mealbox.add(box)

print(mealbox._children)
print(mealbox.get_price())