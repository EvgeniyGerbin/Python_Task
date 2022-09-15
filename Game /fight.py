import sys
from exceptions import InputError
from models import *
import random

print(
    '\nWARRIOR [1]------>Stronger than a wizard but, weaker than a rider!'
    '\nWIZARD[2]-------->Stronger than a archer but, weaker than a warrior!'
    '\nARCHER [3]------->Stronger than a rider but, weaker than a wizard!'
    '\nRider [4]-------->Stronger than a warrior but, weaker than a archer!'
    '\n<====================================================================>'
    '\n Choose your character:'
)
char1 = int(input())

if char1 == 1:
    char1 = warrior
elif char1 == 2:
    char1 = wizard
elif char1 == 3:
    char1 = archer
elif char1 == 4:
    char1 = rider
else:
    raise InputError

char2 = characters[random.randint(0, 3)]
print(f'{char1.name} and {char2.name} will fight!!!')


def menu():
    while True:
        print('1) Let`s Fight!')
        print('2) View info!')
        try:
            n = int(input())

            if n == 1:
                fight()
            if n == 2:
                menu_stats()



        except NameError:
            print('Input int!')
        except SyntaxError:
            print('Input int!')


def menu_stats():
    print('Your character:')
    char1.character_info()
    print('---------------------')
    print("Enemy: ")
    char2.character_info()
    input('Press Enter to continue!')


def fight():
    if char1 == warrior and char2 == wizard:
        char1.damage = char1.damage + (char1.damage * 0.15)
    elif char1 == wizard and char2 == archer:
        char1.damage = char1.damage + (char1.damage * 0.15)
    elif char1 == archer and char2 == rider:
        char1.damage = char1.damage + (char1.damage * 0.15)
    elif char1 == rider and char2 == warrior:
        char1.damage = char1.damage + (char1.damage * 0.15)
    elif char2 == warrior and char1 == wizard:
        char2.damage = char2.damage + (char2.damage * 0.15)
    elif char2 == wizard and char1 == archer:
        char2.damage = char2.damage + (char2.damage * 0.15)
    elif char2 == archer and char1 == rider:
        char2.damage = char2.damage + (char2.damage * 0.15)
    elif char2 == rider and char1 == warrior:
        char2.damage = char2.damage + (char2.damage * 0.15)
    while char1.heath or char2.heath <= 0:
        print(f'{char1.name}: {int(char1.heath)}hp, {char1.damage}dmg')
        print(f'{char2.name}: {int(char2.heath)}hp, {char2.damage}dmg')
        print("**********************")
        print('Press 1 to attack the enemy!')
        n = int(input())
        if n == 1:
            luck = random.randint(0, 100)
            if luck <= char1.luck:
                char2.heath -= char1.damage + (char1.damage * char1.critical)
            else:
                char2.heath -= char1.damage
            luck = random.randint(0, 100)
            if luck <= char2.luck:
                char1.heath -= char2.damage + (char2.damage * char2.critical)
            else:
                char1.heath -= char2.damage
        if char1.heath <= 0:
            print('You lose!')
            sys.exit()
        if char2.heath <= 0:
            print('You win! ')
            sys.exit()


if __name__ == '__main__':
    menu()
