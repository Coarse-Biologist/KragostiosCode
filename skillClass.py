import random
class Skill:
    def __init__(self, skill_name: str, description: str, duration: int, cost: int, damage: int, lingering_damage: int, heal: int,buff: list, debuff: list, skill_attributes_dict: dict):
        
        self.skill_name = skill_name #1
        self.description = description #2
        self.duration = duration #3
        self.cost = cost #4
        self.damage = damage #5
        self.lingering_damage = lingering_damage #6
        self.heal = heal #7
        self.buff = buff #8
        self.debuff = debuff #9
        self.skill_attributes_dict = (f"Skill name: {skill_name}\n Description: {description}\n Duration: {duration} turns \n Cost: {cost} mana points \n Damage: {damage} \n Lingering damage: {lingering_damage}\n Healing: {heal}\n Buffs applied: {buff}\n Debuffs applied: {debuff}")
    def __str__(self):
          return self.skill_attributes_dict
    
    # debuff library
    
    def skill_at_checker(self):
        skill_charactaristic_dict = {}
        if self.duration >= 2:
            skill_charactaristic_dict.setdefault("duration", self.duration)
        if self.cost > 0:
            skill_charactaristic_dict.setdefault("cost", self.cost)
        if self.damage > 0:
            skill_charactaristic_dict.setdefault("damage", self.damage)
        if self.lingering_damage > 0:
            skill_charactaristic_dict.setdefault("lingering damage", self.lingering_damage)
        if self.heal > 0:
            skill_charactaristic_dict.setdefault("heal", self.heal)
        if len(self.buff) > 0:
            skill_charactaristic_dict.setdefault("buff", (self.buff))
        if len(self.debuff) > 0:
            skill_charactaristic_dict.setdefault("debuff", (self.debuff))
        print(self.skill_attributes_dict)
        return skill_charactaristic_dict     
         







#skill library (needs to be organized and expanded)
        
simple_attack = Skill("Attack", "player strikes", 1, 0, 5, 1, 0, [], [], {})

godsmack_attack = Skill("Obliterate", "the divine being strikes", 1, 100, 100, 0, 0, [], [], {})

simple_heal = Skill("Touch of the healer", "player uses a heal", 1, 20, 0, 0, 10, [], [], {})
summon_livingFire = Skill("Summon Living Fire", "Fire and intellect leave you to become an independent, warming force", 20, 60, 0, 0, 0, [], [], {})
    
weak_invis = Skill("Obscure", "You are wrapped in shadow and obscurity", 5, 60, 0, 0, 10, [], ["lower_hitchance1"], {})

tentacle_choke = Skill("Tentacle Choke", "The many-armed monster wraps its tentacles around its target and squeezes with fearful force", 1, 10, 20, 0, 0, [], [], {} ) #octopus_fey and similar creatures have access.





