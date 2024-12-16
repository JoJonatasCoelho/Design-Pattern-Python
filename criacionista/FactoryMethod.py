# tudo que tem factory cria objetos

class IProduto:
    def fale_oi(self):
        ...

class ConcreteProduto(IProduto):
    def fale_oi(self):
        print("Oi")

class ITheCreator:
    def factory_method(self):
        ...

    def CreateAndShow(self):
        print(self.factory_method())
        return self.factory_method()

class ConcreteCreator(ITheCreator):
    def factory_method(self):
        return ConcreteProduto()
    
Tyler = ConcreteCreator()
produt: ConcreteProduto = Tyler.CreateAndShow()

produt.fale_oi()
