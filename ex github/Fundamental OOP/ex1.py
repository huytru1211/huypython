class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travalled_distance = 0

    def __str__(self):
        return f"Registration number {self.registration_number}\nMaximum speed {self.maximum_speed} km/h"

car = Car("ABC-123", 140)
print(car)
print(f"Current speed: {car.current_speed}\nTravelled distance: {car.travalled_distance}")

