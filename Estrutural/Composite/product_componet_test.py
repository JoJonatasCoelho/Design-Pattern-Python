import unittest
from product_componet import *
from faker import Faker

class TestProductComponent(unittest.TestCase):
    def test_leaf(self):
        preco = Faker().random_int(0, 1000) 
        product = ProductLeaf("Produto 1", preco)
        result = product.get_price()
        # self.assertEqual(result, 100)
        assert result == preco
        

if __name__ == '__main__':
    unittest.main()