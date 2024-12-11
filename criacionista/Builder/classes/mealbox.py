from interfaces.meal import MealComposite

class MealBox(MealComposite):

    _children = []


    def get_price(self) -> float:
        soma = 0
        for meal in self._children:
            soma += meal.get_price()

        return float(soma)

    def add(self, meals: MealComposite) -> None:
        for meal in meals:
            self._children.append(meal)