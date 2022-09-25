from models import characters
from models import Army
from collections import Counter
import sys
import time


class Game:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Game.__instance = None

    @staticmethod
    def options():
        press = int(input('1) Try again!\n'
                          '2)To Main Menu\n'
                          '3) Exit game!\n'))
        match press:
            case 1:
                game.duel()
            case 2:
                game.start_game()
            case 3:
                sys.exit()
            case _:
                print('Incorrect input!')

    @staticmethod
    def select_character():
        print(
            '\nWARRIOR [1]------>Stronger than a wizard but, weaker than a rider!'
            '\nWIZARD[2]-------->Stronger than a archer but, weaker than a warrior!'
            '\nARCHER [3]------->Stronger than a rider but, weaker than a wizard!'
            '\nRider [4]-------->Stronger than a warrior but, weaker than a archer!'
            '\n<====================================================================>'
            '\n Choose your character:'
        )
        character = int(input())

        match character:
            case 1:
                character = characters[0]
            case 2:
                character = characters[1]
            case 3:
                character = characters[2]
            case 4:
                character = characters[3]
            case _:
                print('Input incorrect!')
        character.fraction_select()
        return character

    @staticmethod
    def select_character_to_army():
        print(
            '\nWARRIOR [1]------>Stronger than a wizard but, weaker than a rider!'
            '\nWIZARD[2]-------->Stronger than a archer but, weaker than a warrior!'
            '\nARCHER [3]------->Stronger than a rider but, weaker than a wizard!'
            '\nRider [4]-------->Stronger than a warrior but, weaker than a archer!'
            '\n<====================================================================>'
            '\n Choose your character:'
        )
        character = int(input())

        match character:
            case 1:
                character = characters[0]
            case 2:
                character = characters[1]
            case 3:
                character = characters[2]
            case 4:
                character = characters[3]
            case _:
                print('Input incorrect!')
        return character

    @staticmethod
    def info_duel(player, enemy):
        print('Your character:')
        player.__str__()
        print('---------------------')
        print("Enemy: ")
        enemy.__str__()
        print('---------------------')
        game.duel()

    @staticmethod
    def duel():
        char1 = game.select_character()
        char2 = game.select_character()
        print(f'{char1.name} and {char2.name} will fight!!!')
        print('1) Fight!\n'
              '2) View info!\n'
              '3) Exit Game!')

        press = int(input())
        match press:
            case 1:
                game.fight(char1, char2)
            case 2:
                game.info_duel(char1, char2)
            case 3:
                sys.exit()
            case _:
                print('Incorrect input')

    @staticmethod
    def create_army():
        army = []
        while True:
            print('1) Add unit to army\n'
                  '2) Create Army')
            i = int(input())
            match i:
                case 1:
                    army.append(game.select_character_to_army())
                    continue
                case 2:
                    army_damage = 0
                    army_hp = 0
                    b = []
                    most_popular_unit = 0
                    len_army = 0
                    lvl = 0
                    average_level = 0

                    for i in army:
                        army_damage += i.dmg()
                        army_hp += i.get_health()
                        b.append(i.name)
                        most_popular_unit = Counter(b).most_common(1)
                        len_army = len(army)
                        lvl += i.level
                        average_level = lvl // len_army

                    arm = Army(army_hp, army_damage, most_popular_unit[0][0],
                               len_army, average_level, Army.fraction_select())
                    return arm
                case _:
                    print('Incorrect input!')

    @staticmethod
    def army_mod():
        print('Create first army!\n')
        army1 = game.create_army()
        print('Create second army!')
        army2 = game.create_army()
        press = int(input('1) Army Fight!\n'
                          '2) View info!\n'
                          '3) Main menu!'))
        match press:
            case 1:
                game.army_fight(army1, army2)
            case 2:
                army1.__str__()
                print('****************')
                army2.__str__()
                pres = int(input('1) To fight!\n'
                                 '2) To Main Menu!'))
                match pres:
                    case 1:
                        game.army_fight(army1, army2)
                    case 2:
                        game.start_game()
                    case _:
                        print('Incorrect input!')

            case 3:
                game.start_game()
            case _:
                print('Incorrect input')

    @staticmethod
    def check_army(army1, army2):
        if army1.current_health <= 0:
            print(f'Army[{army1.fraction}] defeat!')
            game.options()
        elif army2.current_health <= 0:
            print(f'Army[{army2.fraction}] defeat!')
            game.options()
        elif army2.current_health == 0 and army1.current_health == 0:
            print(f'It`s DRAW!')
            game.options()

    @staticmethod
    def army_fight(army1, army2):
        move = 1
        while True:
            print(f'Move{move}\n'
                  f'Army[{army1.fraction}] deals {army1.damage}\n'
                  f'******************************************')
            army2.current_health -= army1.damage + army1.attack_fraction(army2)
            print(f'Army[{army2.fraction}] have {round(army2.current_health)} hp.\n'
                  f'Army[{army1.fraction}] have {round(army1.current_health)} hp.\n')
            game.check_army(army1, army2)
            move += 1
            time.sleep(1)
            print(f'Move{move}\n'
                  f'Army[{army2.fraction}] deals {army2.damage}\n'
                  f'******************************************')
            army1.current_health -= army2.damage + army2.attack_fraction(army1)
            print(f'Army[{army2.fraction}] have {round(army2.current_health)} hp.\n'
                  f'Army[{army1.fraction}] have {round(army1.current_health)} hp.\n')
            game.check_army(army1, army2)
            move += 1
            time.sleep(1)

    @staticmethod
    def start_game():
        print('Hello!')
        while True:
            print('1) Fight 1vs1')
            print('2) Army Fight!')
            print('3) Exit game!')
            n = input()
            match n:
                case '1':
                    game.duel()
                case '2':
                    game.army_mod()
                case '3':
                    print('Goodbye!')
                    sys.exit()
                case _:
                    print('Incorrect input, please try again!')

    @staticmethod
    def check(player, enemy):
        if player.current_health <= 0:
            enemy.lvl_up()
            player.heal()
            print(f'You lose!\n'
                  f'Enemy level: {enemy.level} ')
            game.options()
        elif enemy.current_health <= 0:
            player.lvl_up()
            enemy.heal()
            print(f'You win!\n'
                  f'Your level: {player.level} ')
            game.options()
        elif enemy.current_health == 0 and player.current_health == 0:
            player.heal()
            enemy.heal()
            print(f'It`s DRAW!')
            game.options()

    @staticmethod
    def fight(player, enemy):
        move = 1
        while True:
            print(f'Move{move}\n'
                  f'{player.name}[{player.fraction}] deals {player.attack(enemy)}\n'
                  f'******************************************')
            enemy.current_health -= player.attack(enemy)
            print(f'{enemy.name}[{enemy.fraction}] have {round(enemy.current_health)} hp.\n'
                  f'{player.name}[{player.fraction}] have {round(player.current_health)} hp.\n')
            game.check(player, enemy)
            move += 1
            time.sleep(1)
            print(f'Move{move}\n'
                  f'{enemy.name} [{enemy.fraction}] deals {enemy.attack(player)}\n'
                  f'******************************************')
            player.current_health -= enemy.attack(player)
            print(f'{player.name}[{player.fraction}] have {round(player.current_health)} hp.\n'
                  f'{enemy.name}[{enemy.fraction}] have {round(enemy.current_health)} hp.\n')
            game.check(player, enemy)
            move += 1
            time.sleep(1)


if __name__ == '__main__':
    game = Game()
    game.start_game()
