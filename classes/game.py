import random

#assigns variables to colors that we can use in terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atklow = atk - 10
        self.atkhigh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        #generating random damage between theese two variables
        return random.randrange(self.atklow, self.atkhigh)

    #index number 'i' because it's an array
    def generate_spell_damage(self, i):
        magicl = self.magic[i]["dmg"] - 5
        magich = self.magic[i]["dmg"] + 5
        return random.randrange(magicl, magich)

    #subtracting the amount of damage from current hp
    def take_damage(self, dmg):
        self.hp -= dmg
        #truth checking
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    #function for choosing a spell
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    # function for getting spell cost
    def get_spell_mpcost(self, i):
        return self.magic[i]["mpcost"]

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def choose_action(self):
        #option starts with 1
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item) #converting index number to string
            i += 1 #incrementing 'i'

    #choosing a magic spell
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["mpcost"]) + ")")
            i += 1







