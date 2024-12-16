class ProductComponet:
    __parent__ = None

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name
    
    def get_chield(self):
        return self.name

    def add(self, parent):
        ...

    def remove(self, parent):
        ...


class ProductLeaf(ProductComponet):
    def get_price(self):
        return self.price

class ProductComposed(ProductComponet):

    children: ProductLeaf = []
    
    def get_price(self):

        child = 0
        for child in range(len(self.children)):
            print(self.children[child].get_price())
        
        total = self.price
        for child in self.children:
            total += child.get_price()
        return total

    def add(self, child):
        self.children.append(child)
        child.__parent__ = self
    
    def remove(self, child):
        self.children.remove(child)
        child.__parent__ = None

    def get_chield(self):
        return self.children

    def get_name(self):
        return self.name

    def __str__(self):
        return f'{self.name}: {self.get_price()}'