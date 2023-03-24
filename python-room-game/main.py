from house import *
from time import *
from random import *

print(" _____       _____        _____       ____  ____        _______      ____      ____  ____     ____")
print("|  _  \     /     \      /     \     /    \/    \      /  ____ \    /    \    /    \/    \   |  __|")
print("| |_|  |   /   _   \    /   _   \   |  /\    /\  |    |  /    \_\  /  /\  \  |  /\    /\  |  | |")
print("|    _/   |   / \   |  |   / \   |  | |  |  |  | |    |  |  ____   | |__| |  | |  |  |  | |  | |__")
print("| |\ \    |   \_/   |  |   \_/   |  | |  |  |  | |    |  | |__  |  |  __  |  | |  |  |  | |  |  __|")
print("| | \ \    \       /    \       /   | |  |  |  | |     \  \__/  /  | |  | |  | |  |  |  | |  | |__")
print("|_|  \_\    \_____/      \_____/    |_|  |__|  |_|      \______/   |_|  |_|  |_|  |__|  |_|  |____|")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")

def boss_room():
    global strength
    global heart
    global currentRoom
    global extraStrength
    global extraWeakness
    global key

    print("  ____       _______        ____       ____   ")
    print(" |  _ \     /       \      / __ \     / __ \  ")
    print(" | / \ \   /   ___   \    / /  \_|   / /  \_| ")
    print(" | \_/ /  |   /   \   |  | |        | |       ")
    print(" |    /   |  |     |  |   \ \___     \ \___   ")
    print(" |  _ \   |  |     |  |    \___ \     \___ \  ")
    print(" | / \ \  |   \___/   |    _   \ \    _   \ \ ")
    print(" | \_/ /   \         /    | \__/ /   | \__/ / ")
    print(" |____/     \_______/      \____/     \____/  ")
    print(r"{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")

    boss_heart = 3

    if "sword" in inventory[1]:
        strength += 4
        if "bow" in inventory[1] and "arrows" in inventory[0]:
            print("Would you like to use your bow, and arrows?")
            if input(">").lower() == "yes":
                strength += 3
                usable.remove("arrows")
                inventory[0].remove("arrows")
            if "Matser-Key" in key:
                strength += 7
        elif "Matser-Key" in key:
            strength += 7
    else:
        heart = 0

    while heart > 0 and boss_heart > 0:
        if usable != None:
            if input("Would you like to use an item? (Yes, or no): ")[0].lower() == "y":
                use(input("Type the item you would like to use: "))
        player_attack = randint(0, strength + extraStrength)
        boss_attack = randint(7, 49 - extraWeakness)
        boss_heart_list = []
        while len(boss_heart_list) < boss_heart:
            boss_heart_list.append("heart")
        
            heart_list = []
            for hearts in boss_heart_list:
                print(" _  _ ", end=" ")
            print()
            for hearts in boss_heart_list:
                print("/ \/ \ ", end="")
            print()
            for hearts in boss_heart_list:
                print("\    /", end=" ")
            print()
            for hearts in boss_heart_list:
                print(" \  / ", end=" ")
            print()
            for hearts in boss_heart_list:
                print("  \/  ", end=" ")
            print()

        print("You have an attack power of", player_attack)
        print("The BOSS has an attack power of", boss_attack)
        if player_attack > boss_attack:
            print("You hurt the BOSS!")
            boss_heart -= 1
        elif player_attack == boss_attack:
            if "sheild" in inventory[0]:
                block = randint(0, 3)
            if block == 2 or block == 3:
                print("You blocked the BOSS!!!")
            else:
                print("You hurt the BOSS, though he also hurt you!!")
                heart -= 1
            boss_heart -= 1
            block = None
        else:
            if "sheild" in inventory[0]:
                block = randint(0, 3)
            if block == 2 or block == 3:
                print("You blocked the BOSS!!!")
            else:
                print("The BOSS hurt you!!!")
                heart -= 1

    extra_strength = 0
    extra_weakness = 0

    if boss_heart == 0:
        print("You killed the boss!!!")
        current_room = 14

def victory_message():
    print("    _____________________")
    print("   /                     \ ")
    print("  /                       \ ")
    print(" /                         \ ")
    print("/___________________________\ ")
    print(" |                         |")
    print(" |    _________________    |")
    print(" |   /                 \   |")
    print(" |  /  \  /\  / | |\ |  \  |")
    print(" |  \   \/  \/  | | \|  /  |")
    print(" |   \_________________/   |")
    print(" |     _______       _      |")
    print(" |    |___|___|     | |     |")
    print(" |____|___|___|_____|_|_____|")
    print("     |          |  |   |")
    print("     |     _    | /   /")
    print("     |   \(\")/  |/   /")
    print("     |     |        /")
    print("     |    / \    __/")
    print("     |__________|")

def death_message():
    print("__   __   _____    _   _     ____    _   ___   ___     _  ")
    print("\ \_/ /  /  _  \  | | | |   |  _ \  | | |  _| |  _ \  | | ")
    print(" \   /  |  / \  | | | | |   | | \ | | | | |_  | | \ | | | ")
    print("  | |   | |   | | | | | |   | | | | | | |  _| | | | | |_| ")
    print("  | |   |  \_/  | | \_/ |   | |_/ | | | | |_  | \_/ | / \ ")
    print("  |_|    \_____/   \___/    |____/  |_| |___| |____/  \_/ ")
    print(r"{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")

strength = 0

def enemy():
    global extraWeakness
    if "toilet-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 5)
    elif "bedroom-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 3)
    elif "cook-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 4)
    elif "chair-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 6)
    elif "tv-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 1)
    elif "food-serving-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 5)
    elif "motercycle-enemy" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 2)
    elif "door-keeper" in house[houseIndex][currentRoom]["enemy"]:
        enemyAttack = randint(0, 7)

    enemyAttack -= extraWeakness
    print(enemyAttack)
    return enemyAttack

def battle():
    global strength
    global heart
    global currentRoom
    global extraStrength
    global extraWeakness
    global key
    global house

    if "enemy" in house[houseIndex][currentRoom]:
        if "sword" in inventory[1]:
            strength += 4
            if "bow" in inventory[1] and "arrows" in inventory[0]:
                print("Would you like to use your bow, and arrows?")
                if input(">").lower() == "yes":
                    strength += 3
                    usable.remove("arrows")
                    inventory[0].remove("arrows")
                if "Master-Key" in key:
                    strength += 1
            elif "Master-Key" in key:
                strength += 7
        elif "broken-sword" in inventory[0]:
            print("You defeated the monster!")
            del house[houseIndex][currentRoom]["enemy"]
            usable.remove("broken-sword")
        
    while "enemy" in house[houseIndex][currentRoom] and heart > -1:
        block = None
        print("You are battling a(n)", house[houseIndex][currentRoom]["enemy"])
        if usable != None:
            if input("Would you like to use an item? (Yes, or no): ")[0].lower() == "y":
                use(input("Type the item you would like to use: "))

        playerAttack = randint(0, strength + extraStrength)
        enemyAttack = enemy()
        print("Your attack power is", playerAttack)
        print("Your enemies attack power is", enemyAttack)

        if playerAttack > enemyAttack:
            del house[houseIndex][currentRoom]["enemy"]
            print("Well done, you defeated an enemy!")
        elif playerAttack == enemyAttack:
            if "sheild" in inventory[0]:
                block = randint(0, 3)
                if block == 2 or block == 3:
                    print("You blocked, and defeated an enemy")
            else:
                heart -= 1
                print(f"You defeated an enemy, but your harts went down to {heart}!")
            del house[houseIndex][currentRoom]["enemy"]
        else:
            if "sheild" in inventory[0]:
                block = randint(0, 3)
            if block == 2 or block == 3:
                print("You blocked an enemy")
            else:
                heart -= 1
                print(f"You lost a heart!! Current heart status is {heart} hearts!")
        
        strength = 0
        extraStrength = 0
        extraWeakness = 0
        if heart < 0:
            return heart

def use(use):
    if use in usable:
        global extraStrength
        global extraWeakness
        #use the item in their inventory
        if use == "super-food":
            extraStrength += 5
        elif use == "food":
            extraStrength += 1
        elif use == "potion":
            extraWeakness += 3
        elif use == "toilet-paper":
            extraWeakness += 1
        elif use == "gas-with-fire":
            extraStrength += 10
        #display a helpful message
        print(use + " used!")
        print("You have an extra strength of", extraStrength)
        print("You deal an extra weekness of", extraWeakness)
        #delete the item from the inventory
        usable.remove(use)
    else:
        print("You can't use that item!")


#starts in hall
currentRoom = 1
#this way you won't die the first round
turns = 0
#a dictionary linking a room to other room positions
houseIndex = 0

def main():
    show_instructions()
    
    global currentRoom
    global inventory
    global key
    global heart
    global usable
    global unusable
    global extraStrength
    
    #loop infinitely
    while True:

        if currentRoom == 14:
            return victory_message()

        #show hearts, inventory, keys, game discription, and room contents.
        show_status()

        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = input(">").split()
        
        if move[0] == "open":
            if move[1] in house[houseIndex][currentRoom] and move[1] == "door":
                print("Over each key hole is a number.")
                print("The numbers are 1 3 3 3 11 3 9 1 2 5")
                print("Put the keys in the correct spot.")
                print("If you place them in the wrong spot you will die!")
                print("Would you like to try now?")
                openDoor = input(">").lower()
                if openDoor == "yes":
                    if len(key) == 11:
                        print("List the keys in order of which slot they belong to.")
                        if input(">").split() == ["challengers-key", "sleepers-key", "cookers-key", "flushers-key", "visitors-key", "pody-key", "toileters-key", "programmers-key", "livers-key", "hungers-key", "drivers-key"] :
                            key.clear()
                            currentRoom = 13
                        else:
                            print("YOU DIED")
                            break
                    else:
                        print("You do not have enough keys!")
        #if they type 'go' first
        elif move[0] == "go":
            #check that they are allowed wherever they want to go
            if move[1] in house[houseIndex][currentRoom]:
                #set the current room to the new room
                if house[houseIndex][currentRoom][move[1]] == "leave":
                    print("Are you sure you want to leave the house? That will make you quit the game.")
                    leave = input(">").lower()
                    if leave == "yes":
                        print("You left the house!")
                        break
                else:
                    currentRoom = house[houseIndex][currentRoom][move[1]]
                    print("You went!")
            #there is no door (link) to the new room
            else:
                print("You can't go that way!")
    
        #if they type 'get' first
        elif move[0] == "get" :
            #if the room contains a usable item, and the item is the one they want to get
            if "usable" in house[houseIndex][currentRoom] and move[1] == house[houseIndex][currentRoom]["usable"]:
                #add the item to their inventory
                usable += [move[1]]
                #display a helpful message
                print(move[1] + " got!")
                #delete the item from the room
                del house[houseIndex][currentRoom]["usable"]
            #if the room contains an unusable item, and the item is the one they want to get
            elif "unusable" in house[houseIndex][currentRoom] and move[1] == house[houseIndex][currentRoom]["unusable"]:
                #add the item to their inventory
                unusable += [move[1]]
                #display a helpful message
                print(move[1] + " got!")
                #delete the item from the room
                del house[houseIndex][currentRoom]["unusable"]
            #otherwise, if the item isn't there to get
            elif "key" in house[houseIndex][currentRoom] and move[1] == house[houseIndex][currentRoom]["key"]:
                #add the key to their storage
                key += [move[1]]
                #display a helpful message
                print(move[1] + " collected!")
                #delete the key from the room
                del house[houseIndex][currentRoom]["key"]
            elif "heart" in house[houseIndex][currentRoom] and move[1] == house[houseIndex][currentRoom]["heart"]:
                #add the heart to their healt bar
                heart += 1
                #display a helpful message
                print(move[1] + " gained!")
                #delete the heart from the room
                del house[houseIndex][currentRoom]["heart"]
            elif "Matser-Key" in house[houseIndex][currentRoom] and move[1] == house[houseIndex][currentRoom]["Master-Key"]:
                #add to keys
                key += "Master-Key"
                #display a helpful message
                print(f"You got the {move[1]}")
                #delete the key from the room
                del house[houseIndex][currentRoom]["secrit-key"]
            else:
                #tell them they can't get it
                print("Can't get " + move[1] + "!")
        #useing an item
        elif move[0] == "use":
            #if an item is usable
            use(move[1])
        elif move[0] == "read" :
            if move[1] in inventory[1]:
                if move[1] == "welcome-note":
                    print("Welcome to my puzzle house. Defeat all the monsters, find all the keays,")
                    print("and defeat me, if you can. I give you the simple-key, and a heart to start.")
                elif move[1] == "journal":
                    print("...Behind the MYSTERIOUS DOOR ROOM is a secrit-key, called Master-Key.")
                    print("It is the only way I can be defeated...")
                elif move[1] == "sword":
                    print("The Sword of This House")
            elif move[1] == "answer":
                print("You have achieved the answer to the puzzle. challengers-key (from the Hall),")
                print("sleepers-key (from the Bedroom), cookers-key (from the Kitchen), flushers-key")
                print("(from the Masters Bathroom), visitors-key (from the Guestroom), pody-key (from")
                print("the Guest Bathroom), toileters-key (from the Bathroom), programmers-key (from")
                print("the Office), livers-key (from the Livingroom), hungers-key (from the")
                print("Diningroom), drivers-key (from the Garage).")
                print()
                print(">challengers-key sleepers-key cookers-key flushers-key visitors-key pody-key toileters-key programmers-key livers-key hungers-key drivers-key")
                print("     ______ _________ _________")
                print("    |Garage|Guestroom|Bathhroom|")
                print("    |______|_________|_________|_______ ___")
                print(" __________ ___________________|MTISO O|BSO|")
                print("|Livingroom|Hall               |YEO ORM|ORM|     N")
                print("|__________|___________________|SRUDRO |SO |     ^")
                print(" __________ _______ _______    |_______|___| W < O > E")
                print("|Diningroom|Kitchen|Bedroom|                     v")
                print("|__________|_______|_______|                     S")

        if currentRoom == 13:
            boss_room()

        battle()

        if heart < 1:
            return death_message()

def show_instructions():
    # comment
    print("Room Game")
    print("=========")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'read [item]'")
def show_status():
    global currentRoom
    global inventory
    global key
    global heart
    #print the player's current status
    print("----------------------------")
    #print the players heart number
    if heart > 0:
        heartList = []
        while len(heartList) < heart:
            heartList.append("heart")
        for hearts in heartList:
            print("/\/\\", end="")
        print()
        for hearts in heartList:
            print("\  /", end="")
        print()
        for hearts in heartList:
            print(" \/ ", end="")
        print()
    print("You are in the " + house[houseIndex][currentRoom]["name"])
    #print the current inventory
    print("Inventory : " + str(inventory))
    #print collected keys
    print("Keys : " + str(key))
    #print an item if there is one
    if "usable" in house[houseIndex][currentRoom]: 
        print("You see a " + house[houseIndex][currentRoom]["usable"] + " in this room")
    if "unusable" in house[houseIndex][currentRoom]: 
        print("You see a " + house[houseIndex][currentRoom]["unusable"] + " in this room")
    if "key" in house[houseIndex][currentRoom]:
        print("There is a " + house[houseIndex][currentRoom]["key"] + " in this room")
    if "heart" in house[houseIndex][currentRoom]:
        print("There is a " + house[houseIndex][currentRoom]["heart"] + " in this room")
    print("----------------------------")

main()
print("Game Over!\nHave a good day!\nHope you play again!")
