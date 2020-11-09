##from os import system
from random import randint

game_title = "Castle dungeons - An interactive fiction game in Python."

# This class will define the basic characteristics of the characters
class Character():
    strength = 5
    magic = 0
    dexterity = 3
    life = 10

    def __init__(self, name, c_class):
        self.name = name
        self.c_class = c_class

    def c_class_char(self):
        if self.c_class == 'Archer':
            self.dexterity = self.dexterity + 6
        elif self.c_class == 'Warrior':
            self.strength = self.strength + 3
            self.life = self.life + 3
        else:
            self.magic = self.magic + 6

    def char_random_upgrade(self):
        print('\nYou have another update available for you character.')
        while True:
            char_to_up = input('\nChoose the characteristic you want to upgrade class:\n(1) Dextery\n(2) Life\n(3) Magic\n(4) Strength\n>>>')
            if char_to_up != '1' and char_to_up != '2' and char_to_up != '3' and char_to_up != '4':
                print('\nInvalid Choice!!! Please select the characteristic to upgrade typing 1, 2, 3 or 4')
                continue
            elif char_to_up == '1':
                input("\nPress Enter to roll a dice to upgrade your Dexterity...")
                roll = randint(1,6)
                self.dexterity = self.dexterity + roll
                print('\nYour rolled {}, your new dextery level is: {}'.format(roll, self.dexterity))
                break
            elif char_to_up == '2':
                input("\nPress Enter to roll a dice to upgrade your Life...")
                roll = randint(1,6)
                self.life = self.life + roll
                print('\nYour rolled {}, your new life level is: {}'.format(roll, self.life))
                break
            elif char_to_up == '3':
                input("\nPress Enter to roll a dice to upgrade your Magic...")
                roll = randint(1,6)
                self.magic = self.magic + roll
                print('\nYour rolled {}, your new magic level is: {}'.format(roll, self.magic))
                break
            elif char_to_up == '4':
                input("\nPress Enter to roll a dice to upgrade your Strength...")
                roll = randint(1,6)
                self.strength = self.strength + roll
                print('\nYour rolled {}, your new strength level is: {}'.format(roll, self.strength))
                break

class Elf(Character):
    race = 'Elf'
    def __init__(self, name, c_class):
        Character.__init__(self, name, c_class)
        self.strength = self.strength + 3
        self.magic = self.magic + 6
        self.dexterity = self.dexterity + 4
        self.life = self.life + 2

class Terran(Character):
    race = 'Terran'
    def __init__(self, name, c_class):
        Character.__init__(self, name, c_class)
        self.magic = self.magic + 5
        self.dexterity = self.dexterity + 6
        self.life = self.life + 4

class Orc(Character):
    race = 'Orc'
    def __init__(self, name, c_class):
        Character.__init__(self, name, c_class)
        self.strength = self.strength + 7
        self.dexterity = self.dexterity + 3
        self.life = self.life + 5

# In this function we will create a character
def character_creation():
    name = input("\nLet's begin...\nWhat is your the name of your character?\n>>>")
    race = define_race()
    c_class = define_class()
    if race == '1':
        player = Elf(name, c_class)
    elif race == '2':
        player = Terran(name, c_class)
    else:
        player = Orc(name, c_class)
    return player

def define_race():
    while True:
        race = input('\nChoose your character race:\n(1) Elf\n(2) Terran\n(3) Orc\n>>>')
        if race != '1' and race != '2' and race != '3':
            print('\nInvalid Choice!!! Please select your character race typing 1, 2, or 3')
            continue
        else:
            break
    return race

def define_class():
    while True:
        c_class = input('\nChoose your character class:\n(1) Archer\n(2) Warrior\n(3) Wizard\n>>>')
        if c_class != '1' and c_class != '2' and c_class != '3':
            print('\nInvalid Choice!!! Please select your character class typing 1, 2 or 3')
            continue
        elif c_class == '1':
            c_class = 'Archer'
            break
        elif c_class == '2':
            c_class = 'Warrior'
            break
        else:
            c_class = 'Wizard'
            break
    return c_class

# Here is define the main structure of the game
def game_intro():
    print('\nWelcome to "{}"'.format(game_title))
    print('\nIn this adventure, you are the hero.\
    \n\nYour choices, skills, and a bit of luck, will influence the outcome of the game.\
    \nAn evil sorcerer is holding your fellow adventurers prisoners.\
    \nWill you succeed to free your friends from the castle dungeons, or peril trying?')
    input('\nPress Enter to select your character...')
    global player
    player = character_creation()
    print("\nNow let's determine your character's skills, which you will use throughout the game.\
    \n\nIn this game, your character has four skills:\
    \n\n- Strength, which you will use in combat or any strength test\
    \n- Dexterity, which you will use in any ability test\
    \n- Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place\
    \n- Life, which determines your life energy, points will be lost when hurt,\
    \nand whenever Life reaches 0, your character dies.\
    \n\nDepending on your race and class, you will have a certain point-base already calculated by the game.\
    \n\nYou will shortly be able to increase your skills by rolling a 6-face die.\
    \n\nHere is your base Character Skills Sheet:")
    #print('\nStrength: {}\nMagic: {}\nDextery: {}\nLife: {}'.format(player.strength, player.magic, player.dexterity, player.life))
    player.c_class_char()
    print('\nName: {}, Race: {}, Class: {}'.format(player.name, player.race, player.c_class))
    print('\nStrength: {}\nMagic: {}\nDextery: {}\nLife: {}'.format(player.strength, player.magic, player.dexterity, player.life))
    player.char_random_upgrade()
    print('\n{} the {} {}. Your start characteristics:'.format(player.name, player.race, player.c_class))
    print('\nStrength: {}\nMagic: {}\nDextery: {}\nLife: {}'.format(player.strength, player.magic, player.dexterity, player.life))
    input('\nPress Enter to start your adventure...')

def chapter_1():
    print('\nYou have entered the Castle Dungeons...\
    \n\nIt is dark, however thankfully your torch is lit and you can see up to 20 feet away from you.\
    \nThe stone walls are damp, the smell of rats and death is strong.\
    \n\nYou walk down a narrow corridor, until you reach a thick stone wall.\
    \nThe corridor continues on the left, and on the right.')
    while True:
        choice = input('\nWhat do you do?\n(1) Turn Left\n(2) Turn Right\n>>>')
        if choice != '1' and choice != '2':
            print('\nInvalid Choice!!! Please select the option typing 1 or 2')
            continue
        elif choice == '1':
            print('\nYou Turned Left')
            Scene_1()
            break
        elif choice == '2':
            print('\nYou Turned Right')
            Scene_2()
            break

def Scene_1():
    print('\nFrom the darkness behind you.. you hear a strange noise.')
    while True:
        choice = input('\nWhat do you do?\n(1) Continue walking\n(2) Stop to listen\n>>>')
        if choice != '1' and choice != '2':
            print('\nInvalid Choice!!! Please select the option typing 1 or 2')
            continue
        elif choice == '1':
            combat()
            break
        elif choice == '2':
            skill_check()
            break

def Scene_2():
    print('\nFrom the darkness ahead of you.. you hear a strange noise.')
    while True:
        choice = input('\nWhat do you do?\n(1) Continue walking\n(2) Stop to listen\n>>>')
        if choice != '1' and choice != '2':
            print('\nInvalid Choice!!! Please select the option typing 1 or 2')
            continue
        elif choice == '1':
            combat()
            break
        elif choice == '2':
            skill_check()
            break

def skill_check():
    print('\nA giant rock falls from the ceiling, roll a dice to see if you can dodge it.. or you will be crashed by it!')
    roll = randint(1,6)
    print('You rolled: {}'.format(roll))
    if (roll + player.dexterity) >= 10:
        print ('\nYou dodge the stone and survive! Danger is not over though...\
        \nThe strange noise in the darkness continues, and it feels a lot closer now...')
        input("\nPress Enter to continue...")
        combat()
    else:
        player.life -= 10
        if player.life > 0:
            print('\nThe Rock crashed you, but you are still alive!!! Danger is not over though...\
            \nThe strange noise in the darkness continues, and it feels a lot closer now...')
            print('Life: {}'.format(player.life))
            input("\nPress Enter to continue...")
            combat()
        else:
            print('\nLife: 0')
            print('You were smashed by the rock.. You die.\n\nGAME OVER')
            input('\nPress Enter to exit the game.')

def combat():
    print('\nA Giant Monster attacks you!')
    input('\nPress Enter to start the combat...')
    monster_level = randint(1,5)
    monster_life = monster_level * 10
    print('Monster Level: {}, Monster Life: {}'.format(monster_level, monster_life))
    print('Character Strength: {}, Life: {}'.format(player.strength, player.life))
    while monster_life > 0 and player.life > 0:
        input('\nPress Enter to attack...')
        player_roll = randint(1,6)
        print('You rolled: {}'.format(player_roll))
        monster_roll = randint(1,6)
        print('The Monster rolled: {}'.format(monster_roll))
        if player_roll > monster_roll:
            print("You hit the monster!")
            monster_life = monster_life - player.strength
            print('Monster Life: {}'.format(monster_life))
        else:
            print('The monster hits you!')
            player.life = player.life - monster_roll
            print('Character Life: {}'.format(player.life))
    if player.life > 0:
        print('\nYou defeated the Giant Monster, Congratulations!!!')
        input('\nPress Enter to exit the game...')
    else:
        print('The Giant Monster defeat you.. You die.\n\nGAME OVER')
        input('\nPress Enter to exit the game.')

def total_game():
    game_intro()
    chapter_1()

total_game()
