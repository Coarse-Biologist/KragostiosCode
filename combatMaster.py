from skillClass import *
from generalFunctions import *
from simplePlayerClass import *
from SummonsClass import *
from creatureClass import *
from printSlowlyFunction import *
from mapCreator import *

class CombatMaster:
    def __init__(self, duration_dict = list):    ## list of dicts
        self.duration_dict = duration_dict
        pass

    def combat_intro(self, player_instance, enemy_list):
        if len(enemy_list) == 1:
            print(f"You see a real gnarly lookin' {enemy_list[0].creature_name}!")
        elif len(enemy_list) == 2:
            if enemy_list[0].creature_name == enemy_list[1].creature_name:
                print(f"You see two real gnarly {enemy_list[0].creature_name}" + "s!")
        else:
            intro_string = "You see a real gnarly group:"
            for i, enemy in enumerate(enemy_list):
                if i == len(enemy_list) -1:
                    if is_vowel(enemy.creature_name[0]):
                        intro_string += " and an " + enemy.creature_name + "."
                        break
                    else:
                        intro_string += " and a " + enemy.creature_name + "."
                        break
                else:
                    if is_vowel(enemy.creature_name[0]):
                        intro_string += " an " + enemy.creature_name 
                    else:
                        intro_string+= " A " + enemy.creature_name + ","
            
    def skill_select(self, player_instance):
        min = 0
        max = len(player_instance.available_actions)
        i = 0
        while i < max:
            for item in player_instance.available_actions:
                if isinstance(item, Skill):
                    print(f"Press {i + 1} to use {item.skill_name}.")
                    i += 1
                elif isinstance(item, Summon):
                    print(f"Press {i + 1} to summon a {item.creature_name}.")
                    i += 1
        choice = choice_int_checker(min,max)
        return choice # returns the INDEX of a skill or summon selected by the player 

    def target_select(self, player_instance, enemy_list):
        self.combatants_list_create(player_instance, player_instance.has_summon, enemy_list)
        print("At whom do you wish to aim this skill?")
        x = 0
        option_number = len(player_instance.has_summon) + len(enemy_list)
        while x < option_number:
            current_option = self.combatants_list[x]
            if "your summon" in current_option:
                print(f"Press {x + 1}: to use skill on {current_option}.")
            else:
                print(f"Press {x + 1}: to use skill on {current_option}.")
            x+=1
        print(f"Press {option_number + 1}: to use skill on yourself.")
        min = 0
        max = option_number
        choice = choice_int_checker(min, max)
        target = self.combatants_list[choice]
        return target

        
    def summon_turn(player_instance):
        the_environment = Map.check_environment()
        for summon in  player_instance.has_summon:          ####### has summon means that they can be summon or that they are summoned?
            creaturefunc = sklz.add_environment_use()
            summon.creaturefunc(the_environment)

    def effect_handler(self, skill_instance): 
        skill_effects_dict = skill_instance.skill_at_checker()
        if "duration" in skill_effects_dict:
            self.duration_counter(self, skill_instance)
        if "cost" in skill_effects_dict:
            self.lose_mana(self, skill_instance)
        if "damage" in skill_effects_dict and "lingering damage" in skill_effects_dict:
            self.cause_all_damage(self, skill_instance)
        if "damage" in skill_effects_dict:
            self.cause_damage(self, skill_instance)
        if "lingering damage" in skill_effects_dict:
            self.cause_lingering_damage(self, skill_instance)
        if "heal" in skill_effects_dict:
            self.heal(self, skill_instance)
        if "buff" in skill_effects_dict:
            self.apply_buff(self, skill_instance)
        if "debuff" in skill_effects_dict:
            self.apply_debuff(self, skill_instance)
        if "push" in skill_effects_dict:
            pass

    def skill_duration_adder(self, skill_instance): 
        counter = skill_instance.duration
        name = skill_instance.skill_name
        self.duration_dict.setdefault(name, counter)
        return self.duration_dict
    def combatants_list_create(self, player_instance, has_summon, enemy_list):
        self.combatants_list = []
        for enemy in enemy_list:
            self.combatants_list.append(enemy.creature_name)
        if len(has_summon) != 0:
            for summon in has_summon:
                self.combatants_list.append(f"{summon.creature_name} (your summon)")
        self.combatants_list.append(player_instance.player_name)
        return self.combatants_list
    
    def duration_counter(self, skill_instance):
        pass

    def lose_mana(self, skill_instance):
        pass

    def cause_damage(self, skill_instance):
        pass

    def cause_lingering_damage(self, skill_instance):
        pass

    def cause_all_damage(self, skill_instance):
        pass

    def heal(self, skill_instance):
        pass

    def apply_buff(self, skill_instance):
        pass

    def apply_debuff(self, skill_instance):
        pass


player1= Player("", (0, 0), 100, 0, 100, 100, 1, 100, 100, 5, [], [simple_attack, godsmack_attack, simple_heal, octopus_fey], [octopus_feyBeta], [])
squealfest = CombatMaster()
enemy_list = [octopus_fey, octopus_feyAlpha, octopus_feyBeta]
#squealfest.skill_select(player1)
squealfest.target_select(player1, enemy_list)

