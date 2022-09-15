class Vehicle:
    __password = 9876
    current_speed = 0
    _boat_current_speed = 2

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return print(f'{self.name} car with maximum speed {self.max_speed} km/h!')

    def run(self):
        self.current_speed = self.max_speed//2
        print(f'The {self.name} has accelerated and is moving at a speed {self.current_speed} km/h')

    @classmethod
    def cls_name(cls):
        return print(cls.__name__)

    @staticmethod
    def summa(x, y):
        return print(x + y)

    def __get_private_password(self):
        return self.__password

    def get_password(self):
        print(self.__get_private_password())

    def _set_password(self, value):
        self.__password = value


class Automobile(Vehicle):

    def __init__(self, name, max_speed, model, year):
        super().__init__(name, max_speed)
        self.model = model
        self.year = year

    def get_info(self):
        return print(f'{self.name} {self.model} {self.year}, max speed {self.max_speed} km/h!' )

    def run(self):
        self.current_speed = self.max_speed // 2.5 + self.current_speed
        print(f'The {self.name} has accelerated and is moving at a speed {self.current_speed} km/h')

    def set_password(self, value):
        self._set_password(value)


class Boat(Vehicle):

    def __init__(self, name, max_speed, sail):
        super().__init__(name, max_speed)
        self.sail = sail

    def run(self):
        self._boat_current_speed = self.max_speed // 2.5
        print(f'The {self.name} has accelerated and is moving at a speed {self._boat_current_speed} km/h')


if __name__ == "__main__":

    #testing the Vehicle class
    bmw = Vehicle('BMW', 250)
    bmw.run()
    bmw.__str__()
    Vehicle.cls_name()
    Vehicle.summa(5, 6)

    print('\n')

    # testing the Automobile class
    VW = Automobile('VW', 180, 'Golf', 2015)
    VW.get_info()
    VW.run()
    VW._set_password(45)
    print('\n')

    # testing the Boat class
    yacht = Boat('Dream', 150, 3)
    yacht.run()
    print('\n')

    #testing private variable methods
    VW.get_password()
    bmw.get_password()
    print('\n')

    # understanding polymorphism
    vehicles = [bmw, VW, yacht]

    for vehicle in vehicles:
        if isinstance(vehicle, Vehicle):
            vehicle.run()