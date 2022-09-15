from enum import Enum
from typing import Union


class BurgerType(Enum):
    AMERICAN = 0,
    CESAR = 1,
    DOUBLECHEESE = 2


class Burger:

    def __init__(self, price: Union[int, float]):
        self.price = price

    def get_price(self):
        return self.price


class AmericanBurger(Burger):
    def __init__(self):
        super().__init__(215.5)


class CesarBurger(Burger):
    def __init__(self):
        super().__init__(189.99)


class DoubleCheeseBurger(Burger):
    def __init__(self):
        super().__init__(195)


def create_burger(burger_type: BurgerType):

    factory_dict = {
        BurgerType.AMERICAN: AmericanBurger,
        BurgerType.DOUBLECHEESE: DoubleCheeseBurger,
        BurgerType.CESAR: CesarBurger
    }
    return factory_dict[burger_type]()
#
# if __name__ == '__main__':
#     for burger in BurgerType:
#         my_burger = create_burger(burger)
#         print(f'{burger}, price: {my_burger.get_price()}')
def char(bur_type: BurgerType):
    factory_dict = {
        BurgerType.AMERICAN: AmericanBurger,
        BurgerType.DOUBLECHEESE: DoubleCheeseBurger,
        BurgerType.CESAR: CesarBurger
    }
    return factory_dict[bur_type]()

burg = char(BurgerType.CESAR)
print(burg.price)