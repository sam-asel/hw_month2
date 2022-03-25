import random


class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        if number <= 0:
            self.__generate_random_number()
            print("Wrong value for address")
        else:
            self.__number = number

    def get_city(self):
        return self.__city

    def set_city(self, value):
        self.__city = value

    def get_street(self):
        return self.__street

    def set_street(self, value):
        if isinstance(value, str):
            if len(value) <= 150:
                self.__street = value
            else:
                print("Wrong value for street it "
                      "must be 150 characters string")
        else:
            print("Wrong value for street it "
                  "must be 150 characters string")

    def get_number(self):
        return self.__number

    def set_number(self, value):
        if value <= 0:
            print("Wrong value for address")
        else:
            self.__number = value

    def __generate_random_number(self):
        self.__number = random.randint(1, 1000)


class Person:
    def __init__(self, address):
        self.__address = address


class Animal:
    def __init__(self, age, name, address):
        self.__age = age
        self.__name = name
        self.__address = address

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            print("Wrong value for age")
        else:
            self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def info(self):
        return f'Name: {self.__name} Age: {self.__age} ' \
               f'City: {self.address.get_city()} ' \
               f'Street: {self.address.get_street()} ' \
               f'Home number: {self.address.get_number()}'

    def speak(self):
        raise NotImplementedError("The method speak must be implemented")


class Fish(Animal):
    def __init__(self, age, name, address):
        super().__init__(age, name, address)

    def speak(self):
        print(f'Fish says nothing')


class Cat(Animal):
    def __init__(self, age, name, address):
        super().__init__(age, name, address)

    def info(self):
        return f'Name: {self.name} ' \
               f'City: {self.address.get_city()} ' \
               f'Street: {self.address.get_street()} ' \
               f'Home number: {self.address.get_number()}'

    def speak(self):
        print(f'Cat says moew')


class Dog(Animal):
    def __init__(self, age, name, address, commands):
        super().__init__(age, name, address)
        self.__commands = commands

    def speak(self):
        print(f'Dog says wouf')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f' Commands {self.__commands}'


address_1 = Address("Bishkek", "Ibraimova", -103)
address_1.set_number(-103)
address_1.set_street("Bokonbaeva")
# address_1.__generate_random_number()

print(f'City: {address_1.get_city()} '
      f'Street: {address_1.get_street()} '
      f'Home number: {address_1.get_number()}')

a_1 = Animal(2, "Tyson", address_1)
a_1.age = 5
print(f'{a_1.age} {a_1.address.get_street()}')
print(a_1.info())

cat_tom = Cat(2, "Tom", Address("LA", "5th Avenue", 21))
print(cat_tom.info())

dog_snoopy = Dog(4, "Snoopy", Address("NY", "Long Avenue", 111), "Sit")
print(dog_snoopy.info())

fish_freddy = Fish(1, "Freddy", Address("Indian Ocean", "No", 2))
print(fish_freddy.info())

animal = [fish_freddy, cat_tom, dog_snoopy]

for a in animal:
    a.speak()
