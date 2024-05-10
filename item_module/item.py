from enum import Enum

class ItemType(Enum):
    WEAPON = 0
    ARMOR = 1
    POTION = 3
    SCROLL = 4
    MISCELANEOUS = 5
    
class ItemRarity(Enum):
    COMMON = 0
    RARE = 1
    LEGENDARY = 2

class Item:
    def __init__(self, name = "", type : ItemType = None, value = 0, rarity = ItemRarity.COMMON) -> None:
        self.name = name
        self.type = type
        self.value = value
        self.sellable = True
        self.rarity = rarity
 


    def getName(self) -> str:
        return self.name
    def setName(self, name : str) -> None:
        self.name = name
    def getType(self) -> ItemType:
        return self.type
    def setType(self, type : ItemType) -> None:
        self.type = type
    def isSellable(self) -> bool:
        return self.sellable
    def setSellable(self, value : bool) -> None:
        self.sellable = value
