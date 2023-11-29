# class Elevator:
#     def __init__(self, bot, top):
#         self.bot = bot
#         self.top = top
#         self.current = bot
#
#     def floor_up(self, target_floor):
#         while target_floor > self.current:
#             self.current = self.current + 1
#             print(f"The elevator is currently at {self.current} floor ")
#
#     def floor_down(self, target_floor):
#         while target_floor < self.current:
#             self.current = self.current - 1
#             print(f"The elevator is currently at {self.current} floor ")
#
#     def go_to_floor(self,target_floor):
#         if target_floor > self.current and target_floor <= self.top:
#             self.floor_up(target_floor)
#         elif target_floor < self.current and target_floor >= self.bot:
#             self.floor_down(target_floor)
#         elif target_floor > self.top or target_floor < self.bot:
#             print(f"The building just have {self.top} floor !!!")
#         else:
#             print(f"The elevator is already floor {self.current}")
#
#
# class Building:
#     def __init__(self, bot, top, elevators):
#         self.bottom_floor = bot
#         self.top_floor = top
#         self.elevators = [Elevator(bot, top) for _ in range(elevators)]
#
#     def run_elevator(self, elevator_number, destination_floor):
#         if 0 <= elevator_number < len(self.elevators):
#             elevator = self.elevators[elevator_number]
#             print(f" Elevator {elevator_number}:")
#             elevator.go_to_floor(destination_floor)
#         else:
#             print(f"Invalid elevator number: {elevator_number}. Please choose a valid elevator.")
#
# building = Building(0,10, 5)
# building.run_elevator(0,7)
# building.run_elevator(1,8)

class Elevator:
    def __init__(self, bot, top):
        self.bot = bot
        self.top = top
        self.current = bot

    def floor_up(self, target_floor):
        while target_floor > self.current:
            self.current = self.current + 1
            print(f"The elevator is currently at {self.current}")

    def floor_down(self, target_floor):
        while target_floor < self.current:
            self.current = self.current - 1
            print(f"The elevator is currently at {self.current}")

    def go_to_floor(self, target_floor):
        if target_floor > self.current and target_floor <= self.top:
            self.floor_up(target_floor)
        elif target_floor < self.current and target_floor >= self.bot:
            self.floor_down(target_floor)
        elif target_floor < self.bot or target_floor > self.top:
            print(f"InValid floor !!")
        elif self.current == target_floor:
            print(f"Already at floor: {self.current}")


# elevator = Elevator(0, 10)
# elevator.go_to_floor(5)
# elevator.go_to_floor(2)

class Building:
    def __init__(self, bot_building, top_building, num_elevators):
        self.bot_building = bot_building
        self.top_building = top_building
        self.num_elevators = num_elevators
        self.elevators = []
        self.elevators = [Elevator(bot_building, top_building) for i in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number <= len(self.elevators):
            print(f"Elevator: {elevator_number}")
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator")

    def add_elevator(self):
        for i in range(self.num_elevators):
            elevator = Elevator(self.bot_building, self.top_building)
            self.elevators.append(elevator)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bot_building)
        print(f"All the elevator is currently at {self.bot_building}")


building = Building(0, 10, 5)
building.run_elevator(3, 9)
building.fire_alarm()
