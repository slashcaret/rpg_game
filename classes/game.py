import random
from typing import Any, Union


class bcolors:
    """
    bcolors is a class with the terminal colors we are going to be using
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightcyan = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    atkh: Union[int, Any]
    
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
    
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        
        if self.hp < 0:
            self.hp = 0
        
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def heal_MP(self, prop):
        self.mp += prop
        if self.mp > self.maxmp:
            self.mp = self.maxmp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, i):
        # self.mp -= i
        self.mp -= self.magic[i].cost
    
    def choose_action(self):
        i = 1
        # print("\n")
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "Actions " + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + " : ", item)
            i += 1
    
    def choose_magic(self):
        i = 1
        # print("\n")
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "Choose Magic " + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + " : {}{}{}{}".format(bcolors.purple, bcolors.BOLD, spell.name, bcolors.ENDC) +
                  "(cost:{} damage:{})".format(spell.cost, spell.dmg))
            i += 1
        
        print("    " + str(0) + " : Enter 0 to return")
    
    def choose_items(self):
        i = 1
        # print("\n")
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "Choose Item " + bcolors.ENDC)
        for each in self.items:
            print(
                "    " + str(i) + " : {}{}{}{}".format(bcolors.purple, bcolors.BOLD, each["item"].name, bcolors.ENDC) +
                " (Description: {}{}{}{})".format(bcolors.purple, bcolors.BOLD, each["item"].description,
                                                  bcolors.ENDC) +
                " *{}{}{}{}".format(bcolors.purple, bcolors.BOLD, each["quantity"], bcolors.ENDC))
            i += 1
        
        print("    " + str(0) + " : Enter 0 to return")
