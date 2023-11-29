class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 2000
        self.travelling_distance = 0

    def __str__(self):
        return f"Registration number: {self.registration_number}\nMaximum speed: {self.maximum_speed} km/h"

    def acceleration(self,change):
        self.new_speed = self.current_speed + change
        self.current_speed = max(0,min(self.new_speed,self.maximum_speed))

    def show_info(self):
        print(f"Current speed of the car: {self.current_speed} km/h")


    def drive(self, hours):
        self.travelling_distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + self.travelling_distance
        print(f"Travelled distance: {self.travelled_distance}")

car = Car("ABC-123", 150)
car.acceleration(60)
car.drive(1.5)
# car.acceleration(50)
# car.acceleration(70)
# car.acceleration(80)
# car.acceleration(-200)
car.show_info()





