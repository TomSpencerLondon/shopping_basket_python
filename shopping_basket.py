from typing import List
from dataclasses import dataclass

@dataclass
class Basket(object):
    items: List

    def total(self):
        return 0