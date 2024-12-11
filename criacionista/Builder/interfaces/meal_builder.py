from abc import ABC, abstractmethod

class MealCompositeBuilder(ABC):
    @abstractmethod
    def get_price():
        raise NotImplementedError("Metodo get price não implementado")
    
    def make_meal(self):
        ...