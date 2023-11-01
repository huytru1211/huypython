
class Elevator:
    def __init__(self, bot, top):
        self.bot = bot
        self.top = top
        self.current = bot

    def floor_up(self, target_floor):
        while target_floor > self.current:
            self.current = self.current + 1
            print(f"The elevator is currently at {self.current} floor ")

    def floor_down(self, target_floor):
        while target_floor < self.current:
            self.current = self.current - 1
            print(f"The elevator is currently at {self.current} floor ")

    def go_to_floor(self,target_floor):
        if target_floor > self.current and target_floor <= self.top:
            self.floor_up(target_floor)
        elif target_floor < self.current and target_floor >= self.bot:
            self.floor_down(target_floor)
        elif target_floor > self.top or target_floor < self.bot:
            print(f"The building just have {self.top} floor !!!")
        else:
            print(f"The elevator is already floor {self.current}")


class Building:
    def __init__(self, bot, top, elevators) :
        self.bot = bot
        self.top = top
        self.number_of_elevator = elevators
        self.elevators= []
        self.elevators = [Elevator(bot, top) for i in range(elevators)]


    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            print(f" Elevator {elevator_number}:")
            elevator.go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator number: {elevator_number}. Please choose a valid elevator.")

    def fire_alarm(self):
        # destination_floor = self.bot
        for elevator in self.elevators:
            elevator.go_to_floor(self.bot)
        print(f"All the elevator is going down")


    # def add_elevator(self):
    #     for i in range(self.number_of_elevator):
    #         elevator = Elevator(self.bot,self.top)
    #         self.elevators.append(elevator)


building = Building(0,10, 5)


building.run_elevator(0,7)
building.run_elevator(1,8)
# print(building.elevators)

# building.fire_alarm()
