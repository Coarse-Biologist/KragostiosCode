
def compareLocations(player_instance, map_instance):
    if player_instance.player_location in map_instance.enemy_locations_list:
        return "danger"
    elif player_instance.player_location in map_instance.merchant_locations_list:
        return "merchant"
    elif player_instance.player_location in map_instance.loot_locations_list:
        return "loot"
    elif player_instance.player_location in map_instance.quest_locations_list:
        return "quest"
    else:
        print("Nothing to see here!")
        return "clear"
    

    ### level up functions ###

    self = 4


def level_up(self):
    self.level +=1
    self.max_xp *= 2
    self.max_hp +=10
    self.hp_regen += 1
    self.max_mana += 10
    self.mana_regen += 1
    self.choose_new_skill(self)
    choose_stat_increase(self)



### for player class ### reequires new attribute for deterining skills available to learn per level

### how will the list change based on level? do skills need another attribute? or shuld i learn how to use lists and dictionairys better

def choose_new_skill(self):
    i = len(self.available_skills)
    options = 0
    while options < i:
        slo.sloprint(f"Press {options + 1} to learn the skill: {self.available_skills[options].skill_name}.")
        #time.sleep(1)
        options += 1
    

    while True:
        decision = input("Choose!")
        
        if decision.isdigit():
            decision = int(decision)
            if i >= decision > 0:
                skill_decision = self.available_skills[decision].skill_name
                slo.sloprint(f"You have learned {skill_decision}!")
                self.available_actions.append(skill_decision)
                return self.available_actions
            else:
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")


##### when leveling up, player can choose to improve one of following stats:
#levelable_stats =[self.max_hp, self.hp_regen, self.max_mana, self.mana_regen]

def choose_stat_increase(self):
    i = len(self.levelable__stats)
    options = 0
    while options < i:
        slo.sloprint(f"Press {options + 1} to improve: {str(self.levelable_stats[options])}.")
        #time.sleep(1)
        options += 1
    

    while True:
        decision = input("Choose!")
        
        if decision.isdigit():
            decision = int(decision)
            if i >= decision > 0:
                if decision == 1:
                    self.max_hp += 20
                    slo.sloprint("Your maximum hitpoints have increased by 20.")
                elif decision == 2:
                    self.hp_regen += 5
                    slo.sloprint("Your health regeneration has increased by 5.")
                elif decision == 3:
                    self.mana += 20
                    slo.sloprint("Your maximum mana have increased by 20.")
                elif decision == 4:
                    self.mana_regen += 5
                    slo.sloprint("Your mana regeneration has increased by 5.")
                
            else:
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")

### function for counting down duration in skill. <8where does it belong?




def check_environment(self):
        print(f"{self.creature_name}) is frantically scanning its surroundings.")
        environment_possibilities = ("jungel", "cliffs", "forest", "canyons", "grasslands", "icy terrain", "muddy terrain", "subterranean caves", "quick sand", "barren wasteland", "cactus-filled desert", "deserted village", "slow-current river", "fast current river")
        the_environment = random.choice(environment_possibilities)
        print(the_environment)
check_environment()

def slow_think():
    text = f"..... \n ....."
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(.4)
    print(" ", end = '\n')
    
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
    
        def target_select(self, player_instance, has_summon, enemy_type):
    
            pass

def check_environment(self): # map Class function
    environment_possibilities = ("jungel", "cliffs", "forest", "canyons", "grasslands", "icy terrain", "muddy terrain", "subterranean caves", "quick sand", "barren wasteland", "cactus-filled desert", "deserted village", "a slowly flowing river", "a treacherously fleet and rocky river")
    the_environment = random.choice(environment_possibilities)
    print(the_environment)
    return the_environment

def use_environment(self, the_environment): # creatureClass skill
    #if the_environment == "jungle":
    #    self.creature_actions.append(climb())
    #elif the_environment == "cliffs":
    #elif the_environment == "forest":
    #elif the_environment == "canyons":
    #elif the_environment == "grasslands":
    #elif the_environment == "icy terrain":
    #elif the_environment == "muddy terrain":
    #elif the_environment == "subterranean caves":
    #elif the_environment == "quick sand":
    #elif the_environment == "barren wasteland":
    #elif the_environment == "cactus-filled desert":
    #elif the_environment == "deserted village":
    #elif the_environment == "a slowly flowing river":
    #elif the_environment == "a treacherously fleet snd rocky river":
        
creature_climb = Skill("Climb", "uses the environment to ascend to high ground", 99, 0, 0, 0, 0, [climb()], [], {})

def climb(self): #buff function
    pass # decrease chance of being hit







