### for player class ### reequires new attribute for deterining skills available to learn per level##

# how will the list change based on level? do skills need another attribute? or shuld i learn how to use lists and dictionairys better

### function for counting down duration in skill. <where does it belong




skill_instance = 1
self = 2
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
    


# player ability direction select

def direction_choice(self):
    cardinal_directions = ()
    print("Whither willst thou go?")
    print("Press 1 to go North")
    print("Press 2 to go South")
    print("Press 3 to go West")
    print("Press 4 to go East")
    
    
def choice_int_checker(min, max):
        choice = input("Choose!")
        while True:
                if isinstance(choice, int):
                    if min < choice <= max:
                            return choice
                    choice = input("Error! Select a viable option!")
                else: 
                    try:
                        choice = int(choice)
                    except ValueError:
                        choice = input("Error! Select a viable option!")
    
    
    
def option_print_iter(option_presenter: str, option_list: tuple, option_number: int):
    print(option_presenter)
    x = 0
    while x < option_number:
        current_option = option_list[x]
        print(f"Press {x + 1}: to {current_option}.")
        x+=1
    min = 0
    max = option_number
    choice_int_checker(min, max)
    
#option_print_iter("Whither willst thou go?", ("go North", "go South", "go West", "go East"), 4)
### list if enemies


#eckel_monster = Creature("Muscle_Drooler", "A ten foot tall, semihumanoid, bent over its front-hands with a long and pointed tail. The entire body is intensely muscle-bound as though cultivated and extremely steroid-infused. The head consists of four eyes located in all quadrants of the head, and a membraneous mouth which opens extends up to one sixth of thr body length and contains a cave of jagged bone teeth.", [sklz.simple_attack], 60, 1)



#option_print_iter("Will you control the summon? Will it control itself?", ("have a controlled summon", "have an independent summon"), 2)

#effect_handler() in combat master should add the ski_instance to the duration_dict in combatMaster

#check if ability in durarion_dict, carry out effect (lingering_dmg), decrement duration_dict"
def cause_lingering_damage(self, skill_instance):  
    self.skill_duration_adder(skill_instance)
    if (skill_instance) in duration_dict:
        return #damage amount as int, target out of scope, 
    
#do i need seperate duration_dicts for each enemy, player and summon?
#if i apply multiple buffs, wach to diffeent enemies, how do i seperate their individual durations?

class Plager:
    def __init__(self):
        pass
    
grogu = Plager()

screech = Plager()

class combatMaster:
    def __init__(self, combatant_dur_dict: list):
        self.combatant_dur_dict = combatant_dur_dict
        
    
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