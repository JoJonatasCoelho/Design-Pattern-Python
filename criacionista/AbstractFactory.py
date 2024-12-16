class IProductA:
    def init(self):
        print("Criada " + __class__ + " A")


class IProductB:
    def init(self):
        print("Criada " + __class__ + " A")


class ProductA(IProductA):
    ...


class ProductB(IProductB):
    ...


class AbstractFactory:
    def create_product_a(self):
        raise NotImplementedError
    
    def create_product_b(self):
        raise NotImplementedError
    

class FactoryT1(AbstractFactory):
    def create_product_a(self):
        return ProductA()
    
    def create_product_b(self):
        return ProductB

    
class FactoryT2(AbstractFactory):
    def create_product_a(self):
        return ProductA()
    
    def create_product_b(self):
        return ProductB
    
