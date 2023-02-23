# from CharGen import Character

armor = {"None": [10, "DEX"], "Light": [12, "DEX"], "Heavy": [15, 0], "Shield": [2, 0]} #armor type: base ac, +mod 
weapons = {"1_hand": [], "2_hand": [], "ranged": []}
role_list = ["Warrior", "Thief", "Zealot", "Mage"]
stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

class Role:

    def __init__(self):
        self.role = ""
        self.hitDie = 0
        self.hp = 0
        self.maxhp = 0
        self.equipment = []
        self.proficienies = [[], [], [], []] # armor, weapons, abilities, checks

    def __repr__(self) -> str:
        return f"""
You are a {self.role}.
You have {self.hp} HP out of {self.maxhp} HP.
Your proficiencies are:
- Armor: {self.proficienies[0]}
- Weapons {self.proficienies[1]}
- Abilties {self.proficienies[2]}
- Checks {self.proficienies[3]}"""

    def warrior(self, con):
        self.role = role_list[0]
        self.hitDie = 10
        self.maxhp = 6 + con
        self.hp = self.maxhp
        self.equipment = ["Armor of your choice","Shield","2 one handed weapons","1 two handed weapon","Smith's kit","Healer's kit","5 rations","3 rolls on Sundries"]
        self.proficienies = [["All"], ["All"], ["STR", "CON"], ["Coordination", "Tactics", "Will"]]
    
    def thief(self, con):
        self.role = role_list[1]
        self.hitDie = 6
        self.maxhp = 4 + con
        self.hp = self.maxhp
        self.equipment = ["Light armor","2 one handed weapons","1 ranged weapon","Ammunition","1 use poison","Thief's kit","5 rations","5 rolls on Sundries"]
        self.proficienies = [["Light", "Shield"], ["All"], ["DEX", "INT"], ["Stealth", "Deception", "Senses", "Tools"]]  
    
    def zealot(self, con):
        self.role = role_list[2]
        self.hitDie = 10
        self.maxhp = 6 + con
        self.hp = self.maxhp
        self.equipment = ["Armor of your choice","Shield","1 one handed simple weapon","Holy symbol (divine focus)","Healer's kit","5 rations","2 rolls on Sundries"]
        self.proficienies = [["All"], ["Simple"], ["WIS", "CHA"], ["Spellcasting", "History", "Insight"]]
        
    
    def mage(self, con):
        self.role = role_list[3]
        self.hitDie = 10
        self.maxhp = 6 + con
        self.hp = self.maxhp
        self.equipment = ["1 one handed simple weapon","A shield or 1 hunting bow","Potionery glassware","Scribe's kit","Spell components","2 rations","1 roll on Sundries"]
        self.proficienies = [["Shield"], ["Simple"], ["CON", "INT"], ["Spellcasting", "Finesse", "Negotiation"]]
          