class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.kilometer_counter = 0

    def drive(self, hours):
        self.kilometer_counter = self.maximum_speed * hours

    def get_kilometer_counter(self):
        return self.kilometer_counter

class ElectricCar(Car):
    def __init__(self,registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

    def drive(self, hours):
        super().drive(hours)

    def get_battery_capacity(self):
        return self.battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume_tank):
        super().__init__(registration_number, maximum_speed)
        self.volume_tank = volume_tank

    def drive(self,hours):
        super().drive(hours)

    def  get_tank_volume(self):
        return self.volume_tank

electricCar = ElectricCar("ABC-15", 180, 52)
gasolineCar = GasolineCar("ACD-123", 165, 32.3)

electricCar.drive(3)
gasolineCar.drive(3)

print(f"Electric Car: {electricCar.get_kilometer_counter()} km")
print(f"Gasoline Car: {gasolineCar.get_kilometer_counter()} km")