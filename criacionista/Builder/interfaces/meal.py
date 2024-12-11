from abc import ABC, abstractmethod

class MealComposite(ABC):
    @abstractmethod
    def get_price():
        raise NotImplementedError("Metodo get price não implementado")