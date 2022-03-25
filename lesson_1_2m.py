class Transport:
    def __init__(self, model, year, color):
        self.year = year  # self.year -> object's attribute
        self.model = model
        self.color = color

    def change_color(self, new_color):  # method
        self.color = new_color


class Rocket(Transport):
    def __init__(self, model, year, color):
        Transport.__init__(self, model, year, color)
        # super(Rocket, self).__init__()
        # super().__init__()

    def fly(self, planet):
        print(f'Rocket {self.model} flying to {planet}')


class Chair:
    def __init__(self, material, height):
        self.material = material
        self.height = height


class Car(Transport):  # sample
    wheels = 4  # class attribute

    def __init__(self, model, year, color, chair, penalties=0.0):  # parameters
        Transport.__init__(self, model, year, color)
        self.penalties = penalties
        self.chair = chair

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    wheels = 8

    def __init__(self, model, year, color, penalties, chair, load_capacity):
        Car.__init__(self, model, year, color, chair, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, product, weight):
        if weight <= self.load_capacity:
            print(f'{product} ({weight} kg) is loaded to truck {self.model}')
        else:
            print(f'You can not load this cargo (Max load capacity: {self.load_capacity})')


def add(num_1, num_2):  # function
    print(num_1 + num_2)


mazda_car = Car("Mazda RX-7", 2021, "Red", Chair("Leasure", 100), 100.5)
bmw_car = Car(model="BMW M-3", year=2019,  color="Gray", chair=Chair("Velure", 90))
print(mazda_car)  # адрес объекта - ссылочная переменная

print(f'{mazda_car.model} {mazda_car.year} {mazda_car.color} '
      f'{mazda_car.penalties}  {mazda_car.wheels}')
# mazda_car.color = "Blue"
mazda_car.change_color(new_color="Blue")
print(f'{mazda_car.model} {mazda_car.year} {mazda_car.color} '
      f'{mazda_car.penalties}  {mazda_car.wheels} \n'
      f'Cars chair: {mazda_car.chair.material} {mazda_car.chair.height}')
print(f'{bmw_car.model} {bmw_car.year} {bmw_car.color} '
      f'{bmw_car.penalties}  {bmw_car.wheels} \n'
      f'Cars chair: {bmw_car.chair.material} {bmw_car.chair.height}')

bmw_car.drive("Tokio")
mazda_car.drive("Bishkek")
mazda_car.drive("Osh")
Car.wheels = 6
gmc_car = Car("GMC 6", 2022, "Yellow", 2900.5)
print(f'{gmc_car.model} {gmc_car.year} {gmc_car.color} '
      f'{gmc_car.penalties} {gmc_car.wheels}')

rocket = Rocket("Dragon rocket", 2022, "Pink")
print(f'{rocket.model} {rocket.color} {rocket.year}')
rocket.change_color("Gray")
print(f'{rocket.model} {rocket.color} {rocket.year}')
rocket.fly("Venus")

# class Person:
#
#     def run(self):
#         print("Running")
#
# person_1 = Person()
# person_1.run()

chair_for_truck = Chair("Tkan", 99)

man_truck = Truck("Man 21", 2002, "Black", 900.0, chair_for_truck, 20000)
print(f'{man_truck.model}, {man_truck.year}, {man_truck.color}, {man_truck.wheels},'
      f' {man_truck.penalties}, {man_truck.load_capacity} \n'
      f'Cars chair: {man_truck.chair.material}, {man_truck.chair.height},')
man_truck.load_cargo("apples", 10000)
