class Car:
    def __init__(self, maximum_speed):
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 2000

    def __str__(self):
        return f"The maximum speed of the car is {self.maximum_speed} km/h"

    def acceleration(self,change):
        new_speed = self.current_speed + change
        self.current_speed = max(0,min(self.maximum_speed,new_speed))

    def drive(self, hours):
        self.traveling_distance = self.current_speed * hours

    def show_info(self):
        print(f"Here is the current speed of the car: {self.current_speed} km/h")
        print(f"Traveled distance: {self.traveled_distance + self.traveling_distance}  km")

    def breaks(self):
        print(f"Breaks immediately => Speed of the car: {self.current_speed} km/h")

car = Car(200)
print(car)
car.acceleration(60)
car.drive(1.5)
car.show_info()

