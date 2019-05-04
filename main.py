import time
import math
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#####################################################################################################
# create black magic
fire = Spell("Fire", 10, 100, "Black")
blizzard = Spell("Blizzard", 11, 130, "Black")
thunder = Spell("Thunder", 15, 170, "Black")
meteor = Spell("Meteor", 15, 170, "Black")
quake = Spell("Quake", 10, 100, "Black")

# create white magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Creating Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully Restores the HP & MP of One Member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully Restores the HP & MP of All Members", 9999)

grenade = Item("Grenade", "weapon", "Deals 500 Damage", 500)

# create players
player_spells = [fire, thunder, meteor, cure, cura]
enemy_spells = [fire, quake, blizzard, cure, cura]

player_items = [{"item": potion, "quantity": 1}, {"item": hipotion, "quantity": 1},
                {"item": superpotion, "quantity": 1}, {"item": elixer, "quantity": 1},
                {"item": hielixer, "quantity": 1}, {"item": grenade, "quantity": 1}
                ]

enemy_items = [{"item": potion, "quantity": 1}, {"item": hipotion, "quantity": 1},
               {"item": elixer, "quantity": 1} ]

player = Person(400, 65, 60, 40, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, enemy_spells, enemy_items)

#####################################################################################################
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS! " + bcolors.ENDC)

while running:
    print("=" * 30)
    
    ################################### Player Choice ###################################
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    # print("you chose ",)
    ################################### Player Attacks ###################################
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + bcolors.BOLD)
        print("You attacked enemy with {} damage points.".format(dmg))
        print(bcolors.ENDC)
    ################################# Player Uses Magic #################################
    elif index == 1:
        current_mp = player.get_mp()
        player.choose_magic()
        magic_choice = input("Choose Magic: ")
        magic_index = int(magic_choice) - 1
        
        if magic_choice == '0':
            continue
        
        else:
            spell = player.magic[magic_index]
            spell_dmg = spell.generate_spell_damage()
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + bcolors.BOLD)
                print("You don't have enough MP...")
                print(bcolors.ENDC)
                continue
            
            if spell.type == "White" and (player.get_hp() < (player.get_max_hp() - 100)):
                player.heal(spell_dmg)
                print(bcolors.OKGREEN + bcolors.BOLD)
                print(
                    "Your HP increased by {} with spell {} which costs {} MP".format(spell.dmg, spell.name, spell.cost))
                print(bcolors.ENDC)
                player.reduce_mp(magic_index)
            elif spell.type == "White" and (player.get_hp() >= (player.get_max_hp() - 100)):
                print("No Need To Use Healing")
                continue
            elif spell.type == "Black":
                print(bcolors.OKBLUE + bcolors.BOLD)
                print("You Attacked Enemy with {} Magic Which Costs {}".format(spell.name, spell.cost))
                print(bcolors.ENDC)
                player.reduce_mp(magic_index)
                enemy.take_damage(spell_dmg)
    
    elif index == 2:
        player.choose_items()
        item_choice = input("Choose Item: ")
        item_index = int(item_choice) - 1
        
        p_hp = player.get_hp()
        p_mhp = player.get_max_hp()
        p_mp = player.get_mp()
        p_mmp = player.get_max_mp()
        
        threshold_hp = p_mhp - math.floor(p_mhp / 2)
        threshold_mp = p_mmp - math.floor(p_mmp / 2)
        
        if item_choice == '0':
            continue
        else:
            ittem = player.items[item_index]["item"]

            if ittem.type == "potion" and (p_hp < threshold_hp):
    
                if player.items[item_index]["quantity"] > 0:
                    player.heal(ittem.prop)
                    player.items[item_index]["quantity"] -= 1
                    print(bcolors.OKGREEN + bcolors.BOLD)
                    print("Your HP increased by {} with {}".format(ittem.name, ittem.prop))
                    print(bcolors.ENDC)
                else:
                    print(bcolors.FAIL + bcolors.BOLD)
                    print("Not Enough {}".format(ittem.name))
                    print(bcolors.ENDC)
                    continue
                    
            elif ittem.type == "potion" and (p_hp >= threshold_hp):
                print("No Need To Use potion")
                continue

            elif ittem.type == "elixer" and ((p_hp < threshold_hp) or (p_mp < threshold_mp)):
    
                if player.items[item_index]["quantity"] > 0:
                    player.heal(ittem.prop)
                    player.heal_MP(ittem.prop)
                    player.items[item_index]["quantity"] -= 1
                    print(bcolors.OKGREEN + bcolors.BOLD)
                    print("Your HP and MP is Full by {} ".format(ittem.name))
                    print(bcolors.ENDC)
                else:
                    print(bcolors.FAIL + bcolors.BOLD)
                    print("Not Enough {}".format(ittem.name))
                    print(bcolors.ENDC)
                    continue
                
            elif ittem.type == "elixer" and ((p_hp >= threshold_hp) or (p_mp >= threshold_mp)):
                print("No Need To Use Elixer")
                continue

            elif ittem.type == "weapon":
    
                if player.items[item_index]["quantity"] > 0:
                    player.items[item_index]["quantity"] -= 1
                    print(bcolors.OKBLUE + bcolors.BOLD)
                    print("You Attacked Enemy with {} Which deals {} damage".format(ittem.name, ittem.prop))
                    print(bcolors.ENDC)
                    enemy.take_damage(ittem.prop)
                else:
                    print(bcolors.FAIL + bcolors.BOLD)
                    print("Not Enough {}".format(ittem.name))
                    print(bcolors.ENDC)
                    continue
                    
    
    ################################### Enemy Attacks ###################################
    time.sleep(0.5)
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD)
    if enemy.get_hp() > 0:
        print("Enemy attacked You with {} damage points.".format(enemy_dmg))
    else:
        print("Enemy Dead!")
        # pass
    print(bcolors.ENDC)
    
    print("--" * 15)
    print("Your Current HP:", player.get_hp())
    print("Your Current MP:", player.get_mp())
    print("Enemy HP: {}/{}".format(enemy.get_hp(), enemy.get_max_hp()))
    print("--" * 15)
    ################################### message Printed ###################################
    if player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD)
        print("You Lost !")
        print(bcolors.ENDC)
        break
    elif enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD)
        print("You Won !")
        print(bcolors.ENDC)
        break
    else:
        continue
    
    # running = False
