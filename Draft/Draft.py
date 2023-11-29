import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.travelling_distance = 0

    def __str__(self):
        return f"Registration number: {self.registration_number}\nMaximum speed: {self.maximum_speed} km/h"

    def acceleration(self,change):
        self.new_speed = self.current_speed + change
        self.current_speed = max(0,min(self.new_speed,self.maximum_speed))

    def show_info(self):
        print(f"Current speed of {self.registration_number}: {self.current_speed} km/h")


    def drive(self, hours):
        self.travelling_distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + self.travelling_distance
        print(f"Travelled distance: {self.travelled_distance}")


cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100,200)
    car = Car(registration_number,maximum_speed)
    cars.append(car)


lead = 0
hour = 1
while lead <= 10000:
    print(f"Hour: {hour}")
    for car in cars:
        random_speed = random.randint(-10, 15)
        car.acceleration(random_speed)
        car.drive(1)
        car.show_info()
        if car.travelled_distance > lead:
            lead = car.travelled_distance
    hour = hour + 1

