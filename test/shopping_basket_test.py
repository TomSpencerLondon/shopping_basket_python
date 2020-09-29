import unittest
from dataclasses import dataclass


@dataclass
class Basket(object):
    pass


class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])

if __name__ == '__main__':
    pass