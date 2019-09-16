from classes.game import Person, bcolors

#instantiating Person class for a mage character
#array for 'magic' each spell has a name, mp cost, damage done
magic = [{"name": "Fire", "mpcost": 10, "dmg": 100},
         {"name": "Blizzard", "mpcost": 10, "dmg": 124},
         {"name": "Frost", "mpcost": 10, "dmg": 100}]

player = Person(460,65,60,34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

#ENDC used to end the text styling
print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("===============================")
    player.choose_action()
    choice = input("Choose action: ")
    #reducing choice by 1 (to start counting from 0)
    index = int(choice) - 1
    print("You chose: ", index)

    #generating some damage
    if index == 0:
        dmg = player.generate_damage()
        #telling enemy to take the damage
        enemy.take_damage(dmg)
        print("You attacked with", dmg, "points of damage. Enemy current HP: ", enemy.get_hp())

        #choose magic, generate spell damage, attack the enemy
    elif index == 1:
        player.choose_magic()
        #wrapping input and reducing it by 1
        magic_choice = int(input("Choose which spell to cast:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        #after we generate the spell damage we need to reduce magic points by some cost
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mpcost(magic_choice)
        #getting current magic points of the player
        current_mp = player.get_mp()
        #if mp is enough cast a spell, otherwise "not enough mp"
        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            #we don't miss the turn, the enemy doesn't attack us, simply skips back to the next iteration (line 19)
            continue
        else:
            player.reduce_mp(cost)
            #telling enemy to take the damage
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell + " did ", str(magic_dmg), " amount of damage" + bcolors.ENDC)

    #enemy is going to attack right now
    enemy_choice = 1
    enemydmg = enemy.generate_damage()
    player.take_damage(enemydmg)
    print("Enemy attacks for: ", enemydmg, "points.")

    #print everyone's HP
    print("-------------------------")
    print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your HP: " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your MP: " + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win !" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lost !" + bcolors.ENDC)
        running = False


    #run only once
    #running = False