import random
import sys
from enum import Enum


class CharacterType(Enum):
    WARRIOR = 0,
    WIZARD = 1,
    ARCHER = 2,
    RIDER = 3


class Character:
    def __init__(self, name, health, damage, critical, luck, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.critical = critical
        self.luck = luck
        self.level = level

    def character_info(self):
        return print(f'Character: {self.name}, level {self.level}\n'
                     f'Health: {self.health}\n'
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

    def fight(self, enemy_obj):
        move = 1
        while self.health or enemy_obj.health <= 0:
            print("**********************")
            print(f'MOVE {move}')
            print(f'{self.name}: {int(self.health)}hp, {self.damage}dmg, level[{self.level}]')
            print(f'{enemy_obj.name}: {int(enemy_obj.health)}hp, {enemy_obj.damage}dmg, level[{enemy_obj.level}]')

            enemy_obj.health -= self.dmg()
            self.health -= enemy_obj.dmg()
            move = move + 1
            if self.health <= 0:
                enemy_obj.lvl_up()
                self.heal()
                print(f'You lose!\n'
                      f'Enemy level: {enemy_obj.level}')
                press = int(input('1) Try again!\n'
                                  '2) Exit game!\n'
                                  ''))
                match press:
                    case 1:
                        game.start_game()
                    case 2:
                        sys.exit()
                    case _:
                        print('Incorrect input!')
            if enemy_obj.health <= 0:
                self.lvl_up()
                enemy_obj.heal()
                print(f'You win!\n'
                      f'Your level: {self.level} ')
                press = int(input('1) Try again!\n'
                                  '2) Exit game!\n'))
                match press:
                    case 1:
                        game.start_game()
                    case 2:
                        sys.exit()
                    case _:
                        print('Incorrect input!')

    def heal(self):
        pass

    def lvl_up(self):
        pass


class Warrior(Character):

    def __init__(self):
        super().__init__('Warrior', 150, 12, 0.15, 30, 1)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Wizard):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)

    def lvl_up(self):
        self.level += 1
        self.health = 150 + self.level * 2
        self.damage = 12 + self.level * 2

    def heal(self):
        self.health = 150
        self.level = 1
        self.damage = 12

class Wizard(Character):

    def __init__(self):
        super().__init__('Wizard', 80, 16, 0.3, 30, 1)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Archer):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)

    def lvl_up(self):
        self.level += 1
        self.health = 80 + self.level * 2
        self.damage = 16 + self.level * 2

    def heal(self):
        self.health = 80
        self.level = 1
        self.damage = 16

class Archer(Character):

    def __init__(self):
        super().__init__('Archer', 100, 15, 0.3, 25, 1)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Rider):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage

        super().fight(enemy_obj)

    def lvl_up(self):
        self.level += 1
        self.health = 100 + self.level * 2
        self.damage = 15 + self.level * 2

    def heal(self):
        self.health = 100
        self.level = 1
        self.damage = 15


class Rider(Character):

    def __init__(self):
        super().__init__('Rider', 160, 18, 0.2, 18, 1)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Warrior):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)

    def lvl_up(self):
        self.level += 1
        self.health = 160 + self.level * 2
        self.damage = 18 + self.level * 2

    def heal(self):
        self.health = 160
        self.level = 1
        self.damage = 18

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
                    char1.fight(char2)
                case '2':
                    print('Your character:')
                    char1.character_info()
                    print('---------------------')
                    print("Enemy: ")
                    char2.character_info()
                    input('Press 1 to continue!\n')
                case '3':
                    print('Goodbye!')
                    sys.exit()
                case _:
                    print('Incorrect input, please try again!')


if __name__ == '__main__':
    game = Game()
    game.start_game()
