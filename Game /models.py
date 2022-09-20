import random
import sys
from enum import Enum


class CharacterType(Enum):
    WARRIOR = 0,
    WIZARD = 1,
    ARCHER = 2,
    RIDER = 3


class Character:
    def __init__(self, name, health, damage, critical, luck):
        self.name = name
        self.health = health
        self.damage = damage
        self.critical = critical
        self.luck = luck

    def character_info(self):
        return print(f'Character: {self.name}\n'
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
            print(f'{self.name}: {int(self.health)}hp, {self.damage}dmg')
            print(f'{enemy_obj.name}: {int(enemy_obj.health)}hp, {enemy_obj.damage}dmg')


            enemy_obj.health -= self.dmg()
            self.health -= enemy_obj.dmg()
            move = move + 1
            if self.health <= 0:
                print('You lose!')
                sys.exit()
            if enemy_obj.health <= 0:
                print('You win! ')
                sys.exit()


class Warrior(Character):

    def __init__(self):
        super().__init__('Warrior', 150, 10, 0.15, 30)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Wizard):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)


class Wizard(Character):

    def __init__(self):
        super().__init__('Wizard', 80, 20, 0.3, 30)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Archer):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)


class Archer(Character):

    def __init__(self):
        super().__init__('Archer', 100, 15, 0.3, 100)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Rider):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage

        super().fight(enemy_obj)


class Rider(Character):

    def __init__(self):
        super().__init__('Rider', 160, 18, 0.2, 18)

    def fight(self, enemy_obj):
        if isinstance(enemy_obj, Warrior):
            self.damage = self.damage + (self.damage * 0.15)
        else:
            self.damage = self.damage
        super().fight(enemy_obj)


def char(char_type: CharacterType):
    char_dict = {
        CharacterType.WARRIOR: Warrior,
        CharacterType.WIZARD: Wizard,
        CharacterType.ARCHER: Archer,
        CharacterType.RIDER: Rider
    }
    return char_dict[char_type]()


warrior = char(CharacterType.WARRIOR)
wizard = char(CharacterType.WIZARD)
archer = char(CharacterType.ARCHER)
rider = char(CharacterType.RIDER)

characters = [warrior, wizard, archer, rider]
