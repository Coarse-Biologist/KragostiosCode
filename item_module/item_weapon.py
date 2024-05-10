from .item import *
from .item_equipable import *


class WeaponType(Enum):
    DAGGER = 0
    AXE = 1
    SWORD = 2

class Weapon(Item, Equipable):
    def __init__(self, name = "", itemType = None, value = 0, rarity = ItemRarity.COMMON, damage = 1, weaponType = None, slot : SlotType = None) -> None:
        super(Item, self).__init__(name, ItemType.WEAPON, value, rarity)
        super(Equipable, self).__init__()
        self.damage = damage
        self.weponType = weaponType

    def getWeaponType(self) -> WeaponType:
        return self.weaponType
    def setWeaponType(self, type) -> None:
        self.weaponType = type
    def getDamage(self) -> int:
        return self.damage
    def setDamage(self, damage) -> None:
        self.damage = damage
    
            
