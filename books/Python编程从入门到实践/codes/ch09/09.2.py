# 09.2.py
# 继承


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def increment_odometer(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        print("gas tank has been filled")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")


# 继承 Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 调用父类的 __init__
        super().__init__(make, model, year)
        self.battery_size = 70  # 子类自己的属性
        self.battery = Battery()

    def describe_battery(self):
        print("Battery Size " + str(self.battery_size))

    # 重写父类的方法
    def fill_gas_tank(self):
        print("this car doesn't have a gas tank")


my_tesla = ElectricCar("tesla", "model_s", 2016)
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
