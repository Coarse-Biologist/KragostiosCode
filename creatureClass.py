import skillClass as sklz

class Creature:

    def __init__(self, creature_name, description: str, creature_actions: list, hp: int, danger_level):

        self.creature_name = creature_name

        self.description = description

        self.creature_actions = creature_actions

        self.hp = hp

        self.danger_level = danger_level

    def add_environment_use(self, the_environment): # creatureClass skill
        if the_environment == "jungle":
            self.creature_actions.append(sklz.climb())
        elif the_environment == "cliffs":
           self.creature_actions.append(sklz.push())
        elif the_environment == "forest":
           self.creature_actions.append(sklz.climb())
        elif the_environment == "canyons":
           self.creature_actions.append(sklz.push())
        elif the_environment == "grasslands":
           pass
        elif the_environment == "icy terrain":
           self.creature_actions.append(sklz.push())
        elif the_environment == "muddy terrain":
           self.creature_actions.append(sklz.push())
        elif the_environment == "subterranean caves":
           self.creature_actions.append(sklz.push())
        elif the_environment == "quick sand":
           self.creature_actions.append(sklz.push())
        elif the_environment == "barren wasteland":
           pass
        elif the_environment == "cactus-filled desert":
           self.creature_actions.append(sklz.push())
        elif the_environment == "deserted village":
           pass
        elif the_environment == "a slowly flowing river":
           self.creature_actions.append(sklz.push())
        elif the_environment == "a treacherously fleet snd rocky river":
           self.creature_actions.append(sklz.push())
        
octopus_feyAlpha = Creature("Alpha Grizzly Octopus", "A fur-covered octopus that prominently displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 40, 1)

octopus_fey = Creature("Grizzly Octopus", "A fur-covered octopus that displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 30, 1)


octopus_feyBeta = Creature("Beta Grizzly Octopus", "A fur-covered octopus that insecurely displays his single beak.", [sklz.simple_attack, sklz.tentacle_choke], 25, 1)

eckel_monster = Creature("Muscle_Drooler", "A ten foot tall, semihumanoid, bent over its front-hands with a long and pointed tail. The entire body is intensely muscle-bound as though cultivated and extremely steroid-infused. The head consists of four eyes located in all quadrants of the head, and a membraneous mouth which opens extends up to one sixth of thr body length and contains a cave of jagged bone teeth.", [sklz.simple_attack], 60, 1)



 