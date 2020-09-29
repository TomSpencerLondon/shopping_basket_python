import unittest
from dataclasses import dataclass

from shopping_basket import Basket

@dataclass
class Item(object):
    unit_price: float
    quantity: 1


class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_single_item_quantity_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)

if __name__ == '__main__':
    pass