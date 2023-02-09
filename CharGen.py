class Character:

    def __init__(self):
        
        self.level = 1

        #ability, ability scores, ability modifiers
        self.abilities = [["STR", 0 , 0], ["DEX", 0 , 0], ["CON", 0 , 0], ["INT", 0 , 0], ["WIS", 0 , 0], ["CHA", 0 , 0]]

    def ability_mod(self, score):
        #key = mod, values = ability score range
        score_to_mod = {-5: [0,1], -4: [2,3], -3: [4,5], -2: [6,7], -1: [8,9], 0: [10,11], 1: [12,13], 2: [14,15], 3: [16,17], 4: [18,19], 5: [20,21], 6: [22,23], 7: [24,25], 8: [26,27], 9: [28,29], 10: [30,31]} 

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
        return "Your {ability} has a score of {score} with a modifier of {mod}. Your updated abilities are now: {list}".format(ability = ability, score = score, mod = mod, list = self.abilities)


test = Character()
modifier = test.input_ability_mod("STR", 2)
print(modifier)
