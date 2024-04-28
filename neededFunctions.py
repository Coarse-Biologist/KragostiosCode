### for player class ### reequires new attribute for deterining skills available to learn per level##

# how will the list change based on level? do skills need another attribute? or shuld i learn how to use lists and dictionairys better

### function for counting down duration in skill. <where does it belong

#effect_handler() in combat master should add the ski_instance to the duration_dict in combatMaster

#check if ability in durarion_dict, carry out effect (lingering_dmg), decrement duration_dict"

#damage amount as int, target out of scope, 
    
#do i need seperate duration_dicts for each enemy, player and summon?
#if i apply multiple buffs, wach to diffeent enemies, how do i seperate their individual durations?

def skill_duration_adder(self, skill_instance): #combatMaster class
    counter = skill_instance.duration
    name = skill_instance.skill_name
    self.duration_dict.setdefault(name, counter)
    return self.duration_dict
    
def decrement_duration(self, skill_duration):
    skill_duration = self.duration_dict.get(skill_instance.skill_name)
    if skill_instance>1:
        skill_duration -= 1
        return skill_duration
    elif skill_duration <= 1:
        duration_dict.pop(skill_instance.skill_name)
        return duration_dict
    

def cause_lingering_damage(self, skill_instance):  
    self.skill_duration_adder(skill_instance)
    if (skill_instance) in duration_dict:

    
    def add_dur_dict(self, combatants_list):
        
        for combatant in combatants_list:
            if isinstance(combatant, Player):
                combatant_name = combatant.player_name
            else:
                combatant_name = combatant.creature_name
            combatant_name = {}

    def combatants_list_create(self, player_instance, has_summon, enemy_list):
        self.combatants_list = ()
        for enemy in enemy_list:
            self.combatants_list.append(enemy.creature_name)
        if len(has_summon) != 0:
            for summon in has_summon:
                self.combatants_list.append(summon.creature_name)
        self.combatants_list.append(player_instance.player_name)
        return self.combatants_list