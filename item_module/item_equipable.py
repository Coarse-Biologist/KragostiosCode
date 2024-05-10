from .item import *
#TODO import effect

class SlotType:
    RIGHT_HAND = 0
    LEFT_HAND = 1
    HEAD = 2
    CHEST = 3
    LEGS = 4
    FEET = 5
    JEWELRY = 6 

class Equipable:
    def __init__(self, slot : SlotType = None) -> None:
        self.listOnHitEffects = [] #TODO = [Buff] or [Effect] ?? 
        self.listWornEffects = [] #TODO = [Buff] or [Effect] ?? maybe lists for buff and debuff
        self.slot = slot

    def getSlotType(self) -> SlotType:
        return self.slot
    def setSlotType(self, slot) -> None:
        self.slot = slot
    def hasOnHit(self) -> None:
        return len(self.listOnHitEffects) > 0
    def getOnHitEffects(self) -> list: #TODO: list[effect]
        return self.listOnHitEffects
    def setOnHitList(self, listEffects : list) -> None:
        self.listOnHitEffects = listEffects
    #def addOnHitEffect(self, newEffect) -> None: 
    #    if isinstance(newEffect, effect):      #TODO <= missing effect class here 
    #        self.listOnHitEffects.append()
    #    else isinstance(newEffect, list):
    #        self.listOnHitEffects.extend(newEffect)
    def hasWornEffects(self) -> bool:
        return len(self.listWornEffects) > 0
    def getWornEffects(self) -> list:
        return self.listWornEffects
    def setWornList(self, listEffects : list) -> None:
        self.listWornEffects = listEffects
    #def addWornEffect(self, newEffect) -> None: 
    #    if isinstance(newEffect, effect):      #TODO <= missing effect class here 
    #        self.listWornEffects.append()
    #    else isinstance(newEffect, list):
    #        self.listWornEffects.extend(newEffect)