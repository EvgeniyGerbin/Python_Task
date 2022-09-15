class PersonSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        PersonSingleton.__instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return print(f'Name: {self.name} \n Age: {self.age}')

if __name__ == '__main__':
    vasya = PersonSingleton('Vasya', 21)
    vova = PersonSingleton('Vova', 15)

    print(vasya is vova)
