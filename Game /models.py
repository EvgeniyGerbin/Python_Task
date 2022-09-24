import random
import sys
import time
from enum import Enum


class CharacterType(Enum):
    WARRIOR = 0,
    WIZARD = 1,
    ARCHER = 2,
    RIDER = 3


class Character:
    def __init__(self, name, health, damage, critical, luck, level):
        self.name = name
        self._health = health
        self.current_health = health
        self.damage = damage
        self.critical = critical
        self.luck = luck
        self.level = level

    def get_health(self):
        return self._health

    def set_health(self, value):
        self._health = value

    def __str__(self):
        return print(f'Character: {self.name}, level {self.level}\n'
                     f'Health: {self.current_health}\n'
                     f'Damage: {self.damage}\n'
                     f'Critical damage: {round(self.critical * 100)}%\n'
                     f'Luck: {self.luck}%')

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage * self.critical)
            return crit
        else:
            return self.damage

    def heal(self):
        self.current_health = self.get_health()
        self.level = 1

    def lvl_up(self):
        self.level += 1
        self.current_health = self.get_health() + self.get_health() * 0.15
        self.damage = self.damage + self.damage * 0.10


class Warrior(Character):

    def __init__(self):
        super().__init__('Warrior', 150, 12, 0.15, 30, 1)

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            return self.dmg() + (self.damage * 0.15)
        else:
            return self.dmg()


class Wizard(Character):

    def __init__(self):
        super().__init__('Wizard', 80, 16, 0.3, 30, 1)

    def attack(self, enemy):
        if isinstance(enemy, Archer):
            return self.dmg() + (self.damage * 0.15)
        else:
            return self.dmg()


class Archer(Character):

    def __init__(self):
        super().__init__('Archer', 100, 15, 0.3, 25, 1)

    def attack(self, enemy):
        if isinstance(enemy, Rider):
            return self.dmg() + (self.damage * 0.15)
        else:
            return self.dmg()


class Rider(Character):

    def __init__(self):
        super().__init__('Rider', 160, 18, 0.2, 18, 1)

    def attack(self, enemy):
        if isinstance(enemy, Warrior):
            return self.dmg() + (self.damage * 0.15)
        else:
            return self.dmg()


def char(char_type: CharacterType):
    char_dict = {
        CharacterType.WARRIOR: Warrior,
        CharacterType.WIZARD: Wizard,
        CharacterType.ARCHER: Archer,
        CharacterType.RIDER: Rider
    }
    return char_dict[char_type]()


characters = [char(CharacterType.WARRIOR),
              char(CharacterType.WIZARD),
              char(CharacterType.ARCHER),
              char(CharacterType.RIDER)]


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
                          '2) Exit game!\n'))
        match press:
            case 1:
                game.start_game()
            case 2:
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
        char1 = int(input())

        match char1:
            case 1:
                char1 = characters[0]
            case 2:
                char1 = characters[1]
            case 3:
                char1 = characters[2]
            case 4:
                char1 = characters[3]
            case _:
                print('Input incorrect!')

        return char1

    def start_game(self):
        char1 = self.select_character()
        char2 = characters[random.randint(0, 3)]
        print(f'{char1.name} and {char2.name} will fight!!!')
        while True:
            print('1) Let`s Fight!')
            print('2) View info!')
            print('3) Exit game!')
            n = input()
            match n:
                case '1':
                    game.fight(char1, char2)
                case '2':
                    print('Your character:')
                    char1.__str__()
                    print('---------------------')
                    print("Enemy: ")
                    char2.__str__()
                    input('Press 1 to continue!\n')
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
                  f'{player.name} deals {player.attack(enemy)}\n'
                  f'******************************************')
            enemy.current_health -= player.attack(enemy)
            print(f'{enemy.name} have {round(enemy.current_health)} hp.\n'
                  f'{player.name} have {round(player.current_health)} hp.\n')
            game.check(player, enemy)
            move += 1
            time.sleep(1)
            print(f'Move{move}\n'
                  f'{enemy.name} deals {enemy.attack(player)}\n'
                  f'******************************************')
            player.current_health -= enemy.attack(player)
            print(f'{player.name} have {round(player.current_health)} hp.\n'
                  f'{enemy.name} have {round(enemy.current_health)} hp.\n')
            game.check(player, enemy)
            move += 1
            time.sleep(1)


if __name__ == '__main__':
    game = Game()
    game.start_game()
