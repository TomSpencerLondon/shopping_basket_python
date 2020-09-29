from typing import List
from dataclasses import dataclass

@dataclass
class Basket(object):
    items: List

    def total(self):
        if len(self.items) > 0:
            return self.items[0].unit_price
        return 0