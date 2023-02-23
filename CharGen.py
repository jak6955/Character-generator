import random
from dice import die_roll, dice_roller, stat_gen, alt_stat_gen
from classes import Role

#key = mod, values = ability score range
score_to_mod = {-5: [0,1], -4: [2,3], -3: [4,5], -2: [6,7], -1: [8,9], 0: [10,11], 1: [12,13], 2: [14,15], 3: [16,17], 4: [18,19], 5: [20,21], 6: [22,23], 7: [24,25], 8: [26,27], 9: [28,29], 10: [30,31]} 

#ability, ability scores, ability modifiers
abilities_all = [["STR", 0 , 0], ["DEX", 0 , 0], ["CON", 0 , 0], ["INT", 0 , 0], ["WIS", 0 , 0], ["CHA", 0 , 0]]
stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

#class list | role = class
role_list = ["Warrior", "Thief", "Zealot", "Mage"]

class Character:

    def __init__(self):
        
        self.name = ""
        self.level = 1
        self.proficiency = 2
        self.abilities = abilities_all
        self.role = Role()
        self.AC = 0

    def ability_mod(self, score):

        mod = 0
        #iterate through modifiers to find if the ability score is present, and return the ability modifier
        for key in score_to_mod.keys():
            if score in score_to_mod[key]:
                mod = key
        return mod
    
    #input ability (e.g STR) and its score to update ability with score and modifier
    def input_ability_mod(self, ability, score):
        mod = self.ability_mod(score)
        for group in self.abilities:
            if group[0] == ability:
                group[1] = score
                group[2] = mod
        return
    
    #ask roll method, input ability and abiltiy mod
    def input_stats(self):
        stat_list = []
        gen_type = int(input("For your character's stats, would you like to roll [1] 3d6 in order, or [2] 4d6 drop lowest in order? Please type the corrosponding number: "))

        while stat_list == []:
            if gen_type == 1:
                stat_list = stat_gen()
            elif gen_type == 2:
                stat_list = alt_stat_gen()
            else:
                gen_type = int(input("For your character's stats, would you like to roll [1] 3d6 in order, or [2] 4d6 drop lowest in order? Please type the corrosponding number: "))
        
        for i in range(len(stat_list)):
            a = stats[i]
            s = stat_list[i]
            self.input_ability_mod(a,s)
        return
    
    #return abilities list as [Ability: Score (Modifier)]
    def abilities_ref(self):
        ref_string = "Your abilities are: \n"
        for i in self.abilities:
            stat = i[0]
            score = format(i[1], '02d') # return 1 as 01
            mod = i[2]
            if mod < 0:
                new_string = f"{stat}: {score} ({mod}) \n"
            else:
                new_string = f"{stat}: {score} (+{mod}) \n"
            ref_string += new_string
        return ref_string

    # determine role
    def det_role(self):
        role = int(input("Please choose your character's class: [1] Warrior, [2] Thief, [3] Zealot, [4] Mage. Please type the corrosponding number: "))
        while 0 < role < 5:
            if role == 1:
                self.role.warrior(pc.abilities[2][2])
                role = 0
            elif role == 2:
                self.role.thief(pc.abilities[2][2])
                role = 0
            elif role == 3:
                self.role.zealot(pc.abilities[2][2])
                role = 0
            elif role == 4:
                self.role.mage(pc.abilities[2][2])
                role = 0
        return
    
    



pc = Character()
pc.input_stats()
print(pc.abilities_ref())
pc.det_role()
print(pc.role.__repr__())

