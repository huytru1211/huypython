import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.traveled_distance = 0
        self.current_speed = 0

    def __str__(self):
        return f" Here is the maximum speed of {registration_number}: {maximum_speed} km/h"
    def acceleration(self, change):
        new_speed = self.current_speed + change
        self.current_speed = max(0, min(self.maximum_speed, new_speed))
        return self.current_speed

    def drive(self, hour):
        self.traveling_distance = self.current_speed * hour
        self.traveled_distance = self.traveling_distance + self.traveled_distance

    def show_info(self):
        print(f"Here is the current speed of the car: {self.current_speed} km/h")
        print(f"Traveled distance of {self.registration_number}: {self.traveled_distance}  km ")

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hour = 1
        self.is_Racing = True
        self.lead_car = 0

    def house_passes(self):
        if self.hour % 10 == 0:
            self.current_hour()
        for c in self.cars:
            c.acceleration(random.randint(-10, 15))
            c.drive(1)
            if self.hour%10 == 0:
                c.show_info()
            if self.lead_car < c.traveled_distance:
                self.lead_car = c.traveled_distance

        if self.lead_car > self.distance:
            self.is_Racing = False

        self.hour = self.hour + 1

    def current_hour(self):
        print(f"Hour: {self.hour}")



cars = []
for i in range(1,11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100,200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

race = Race("A1", 10000, cars)
race1 = Race("A2",15000, cars)

while race.is_Racing:
    race.house_passes()
    race1.house_passes()