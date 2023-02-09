import random

def die_roll():
    N = int(input("Enter die size: "))
    die_value = random.choice(range(1, N+1))
    return die_value

def dice_roller():
    #format ndN e.g. 3d6
    n = int(input("Enter number of dice: "))
    N = int(input("Enter die size: "))
    dice_log = []

    # roll ndN nice returning list and sum
    for die in range(0, n):
        dice_value = random.choice(range(1, N+1))   
        dice_log.append(dice_value)
    return sum(dice_log)

#generate list of 6x 3d6
def stat_gen():
    stat_log = []
    
    #for 6 stats
    for stat in range(6):
        #roll 3d6 and sum
        dice_log = []
        for dice in range(3):
            dice_value = random.choice(range(1, 7))   
            dice_log.append(dice_value)
        stat_log.append(sum(dice_log))
    return stat_log
