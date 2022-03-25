class MusicPlayable:
    def play_music(self, song):
        print(f'Now playing {song}')

    @staticmethod
    def add(num1, num2):
        print(num2 + num1)


class Car(MusicPlayable):
    def __init__(self, year, model):
        self.__year = year
        self.__model = model

    def drive(self):
        print(f'{self.model} I am driving')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def __str__(self):
        return f'Model: {self.model} Year: {self.year}';

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __del__(self):
        print(f'{self.model} deleted')


class FuelCar(Car):
    __gas_station = 500

    @staticmethod
    def fuel_type():
        print("AI - 95")

    @classmethod
    def put_fuel(cls, car, amount):
        car.fuel_amount = car.fuel_amount + amount
        cls.__gas_station = cls.__gas_station - amount
        print(f'Gas statios has {cls.__gas_station}')

    def __init__(self, year, model, fuel_amount):
        Car.__init__(self, year, model)
        self.__fuel_amount = fuel_amount

    def drive(self):
        print(f'{self.model} I am driving by fuel')

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self.__fuel_amount = value

    def __str__(self):
        return super(FuelCar, self).__str__() + f' Fuel amount: {self.fuel_amount}'

    def __add__(self, other):
        return self.fuel_amount + other.fuel_amount


class ElectricCar(Car):
    def __init__(self, year, model, battery):
        Car.__init__(self, year, model)
        self.__battery = battery

    def drive(self):
        print(f'{self.model} I am driving by electricity')

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def __str__(self):
        return super(ElectricCar, self).__str__() + f' Battery: {self.battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, year, model, fuel_amount, battery):
        FuelCar.__init__(self, year, model, fuel_amount)
        ElectricCar.__init__(self, year, model, battery)


class SmartPhone(MusicPlayable):
    pass


camry_car = FuelCar(2020, "Camry 80", 45)
print(camry_car)
camry_car.drive()
tesla_car = ElectricCar(2022, "Model X", 700000)
print(tesla_car)
tesla_car.drive()
prius_car = HybridCar(2020, "Toyota Prius HB", 40, 500000)
print(prius_car)
print(id(prius_car))
prius_car.drive()

print(HybridCar.mro())
# print(HybridCar.__mro__)

print(camry_car > prius_car)
print(camry_car + prius_car)
camry_car.play_music("Yesterday")
my_phone = SmartPhone()
my_phone.play_music("My song")

FuelCar.put_fuel(camry_car, 10)
print(camry_car)
FuelCar.put_fuel(prius_car, 20)
print(prius_car)
FuelCar.fuel_type()
MusicPlayable.add(2, 1)

