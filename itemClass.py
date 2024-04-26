import numpy as num
import time

class LootableItem:
    def __init__(self, item_name: dict):
        self.item_name = item_name

gold_coin = LootableItem({"Gold": num.random.randint(1,15)})

