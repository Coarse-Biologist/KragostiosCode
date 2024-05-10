from .item import *
from .item_equipable import *

class ArmorType(Enum):
    IRON = 0
    EFLISH = 1
    LEATHER = 2

class Armor(Item, Equipable):
    def __init__(self, name = "", itemType = None, value = 0, rarity = ItemRarity.COMMON, armorValue = 1, armorType = None, slot : SlotType = None) -> None:
        super(Item, self).__init__(name, ItemType.ARMOR , value, rarity)
        super(Equipable, self).__init__()
        self.armorValue = armorValue
        self.armorType = armorType

    def setArmorType(self) -> ArmorType:
        return self.armorType
    def setArmorType(self, type) -> None:
        self.armorType = type
    def getArmorValue(self) -> int:
        return self.armorValue
    def setArmorValue(self, armor) -> None:
        self.armorValue = armor
    
            
