import random
from enum import Enum


class CharacterType(Enum):
    WARRIOR = 0,
    WIZARD = 1,
    ARCHER = 2,
    RIDER = 3


class Character:
    def __init__(self, name, health, damage, critical, luck, level, fraction):
        self.name = name
        self._health = health
        self.current_health = health
        self.damage = damage
        self.critical = critical
        self.luck = luck
        self.level = level
        self.fraction = fraction

    def get_health(self):
        return self._health

    def set_health(self, value):
        self._health = value

    def __str__(self):
        return print(f'Character: {self.name}, level {self.level}\n'
                     f'Health: {self.current_health}\n'
                     f'Damage: {self.damage}\n'
                     f'Critical damage: {round(self.critical * 100)}%\n'
                     f'Luck: {self.luck}%\n'
                     f'Fraction: {self.fraction}')

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage * self.critical)
            return crit
        else:
            return self.damage

    def fraction_select(self):
        if self.fraction == 'renegade':
            print('Choose a faction, each faction has an advantage over the other:\n'
                  ' white over red, red over blue and blue over white, 5% damage each.\n'
                  '1) White\n'
                  '2) Red\n'
                  '3) Blue\n')
            frac = int(input())
            match frac:
                case 1:
                    self.fraction = 'white'
                case 2:
                    self.fraction = 'red'
                case 3:
                    self.fraction = 'blue'
                case _:
                    print('Incorrect input!')

    def heal(self):

        self.current_health = self.get_health()

    def lvl_up(self):
        self.level += 1
        self.set_health(self.get_health() * 1.15)
        self.current_health = self.get_health()
        self.damage = self.damage * 1.10

    def attack_fraction(self, enemy):
        match (self.fraction, enemy.fraction):
            case ('white', 'red'):
                return self.damage * 0.05
            case ('red', 'blue'):
                return self.damage * 0.05
            case ('blue', 'white'):
                return self.damage * 0.05
            case _:
                return 0

class Warrior(Character):

    def __init__(self):
        super().__init__('Warrior', 150, 12, 0.15, 30, 1, 'renegade')

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            return self.dmg() + (self.damage * 0.15) + self.attack_fraction(enemy)
        else:
            return self.dmg() + self.attack_fraction(enemy)


class Wizard(Character):

    def __init__(self):
        super().__init__('Wizard', 80, 16, 0.3, 30, 1, 'renegade')

    def attack(self, enemy):
        if isinstance(enemy, Archer):
            return self.dmg() + (self.damage * 0.15) + self.attack_fraction(enemy)
        else:
            return self.dmg() + self.attack_fraction(enemy)


class Archer(Character):

    def __init__(self):
        super().__init__('Archer', 100, 15, 0.3, 25, 1, 'renegade')

    def attack(self, enemy):
        if isinstance(enemy, Rider):
            return self.dmg() + (self.damage * 0.15) + self.attack_fraction(enemy)
        else:
            return self.dmg() + self.attack_fraction(enemy)


class Rider(Character):

    def __init__(self):
        super().__init__('Rider', 160, 18, 0.2, 18, 1, 'renegade')

    def attack(self, enemy):
        if isinstance(enemy, Warrior):
            return self.dmg() + (self.damage * 0.15) + self.attack_fraction(enemy)
        else:
            return self.dmg() + self.attack_fraction(enemy)

class Army:

    def __init__(self, health, damage, popular, len_army, average_level, fraction):
        self.health = health
        self.damage = damage
        self.fraction = fraction
        self.popular = popular
        self.len_army = len_army
        self.average_level = average_level
        self.current_health = health

    def __str__(self):
        return print(f'Army [{self.fraction}]\n'
                     f'Hp: {self.health}\n'
                     f'Damage: {self.damage}\n'
                     f'Popular Unit: {self.popular}\n'
                     f'Length Army: {self.len_army}\n'
                     f'Average lvl: {self.average_level}')

    def attack_fraction(self, enemy):
        match (self.fraction, enemy.fraction):
            case ('white', 'red'):
                return self.damage * 0.05
            case ('red', 'blue'):
                return self.damage * 0.05
            case ('blue', 'white'):
                return self.damage * 0.05
            case _:
                return 0

    @staticmethod
    def fraction_select():
            print('Choose a faction for your army: \n'
                  '1) White\n'
                  '2) Red\n'
                  '3) Blue\n')
            frac = int(input())
            match frac:
                case 1:
                    return 'white'
                case 2:
                    return 'red'
                case 3:
                    return 'blue'
                case _:
                    print('Incorrect input!')

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

