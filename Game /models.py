from enum import Enum

class CharacterType(Enum):
    WARRIOR = 0,
    WIZARD = 1,
    ARCHER = 2,
    RIDER = 3


class Character:
    def __init__(self, name, health, damage, critical, luck):
        self.name = name
        self.heath = health
        self.damage = damage
        self.critical = critical
        self.luck = luck

    def character_info(self):
        return print(f'Character: {self.name} \n'
                     f'Health: {self.heath}\n'
                     f'Damage: {self.damage}\n'
                     f'Critical damage: {round(self.critical * 100)}%\n'
                     f'Luck: {self.luck}%')

class Warrior(Character):

    def __init__(self):
        super().__init__('Warrior', 150, 17, 0.15, 15)

class Wizard(Character):

    def __init__(self):
        super().__init__('Wizard', 80, 20, 0.3, 10)

class Archer(Character):

    def __init__(self):
        super().__init__('Archer', 100, 15, 0.3, 20)

class Rider(Character):

    def __init__(self):
        super().__init__('Rider', 160, 18, 0.2, 18)


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


