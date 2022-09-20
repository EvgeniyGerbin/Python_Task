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

match char1:
    case 1:
        char1 = warrior
    case 2:
        char1 = wizard
    case 3:
        char1 = archer
    case 4:
        char1 = wizard
    case _:
        print('Input incorrect!')


char2 = characters[random.randint(0, 3)]


def menu():
    print(f'{char1.name} and {char2.name} will fight!!!')
    while True:
        print('1) Let`s Fight!')
        print('2) View info!')
        n = input()
        match n:
            case '1':
                char1.fight(char2)
            case '2':
                menu_stats()
            case _:
                print('Incorrect input, please try again!')


def menu_stats():
    print('Your character:')
    char1.character_info()
    print('---------------------')
    print("Enemy: ")
    char2.character_info()
    input('Press Enter to continue!')

if __name__ == '__main__':
    menu()
