from functools import reduce
from typing import List
from dataclasses import dataclass
from item import Item


@dataclass
class Basket(object):
    items: List[Item]

    def total(self):
        return reduce(lambda subtotal,
                             item: subtotal + (item.unit_price * item.quantity),
                      self.items, 0)
