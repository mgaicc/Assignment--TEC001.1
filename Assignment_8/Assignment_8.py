class Elevator:
    def __init__(self,bottom_floor:int,top_floors:int):
        self.bottom_floor = bottom_floor
        self.top_floors = top_floors
        self.floor = 0
    def floor_up(self,floor):
        while self.floor != floor:
            self.floor += 1
            print(f'You now go up to floor {self.floor}')
    def floor_down(self,floor):
        while self.floor != floor:
            self.floor -= 1
            print(f'You now go down to floor {self.floor}')
    def go_to_floor(self,floor):
        if self.floor > floor:
            self.floor_down(floor)
        else:
            self.floor_up(floor)
    def fire_alarm(self):
        self.floor_down(0)
        print(f'The building is on fire, the elevator will automatically go to floor 0')
    def display_info(self):
        print(f'You are on floor: {self.floor}')
class Building:
    def __init__(self,bottom_floors:int,top_floors:int,numbers_of_elevator:int):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.numbers_of_elevators = numbers_of_elevator
        self.elevators = []
        for _ in range(1,self.numbers_of_elevators):
            self.elevators.append(Elevator(self.bottom_floors,self.top_floors))
    def run_elevator(self,elevator_numbers:int,destinations_floors:int):
        for elevator in self.elevators:
            elevator = self.elevators[elevator_numbers - 1]
            elevator.go_to_floor(destinations_floors)
            print(f'Your elevator {elevator_numbers} is on floor {elevator.floor}')

        
h = Elevator(0,10)
h.go_to_floor(4)
h.display_info()
h.go_to_floor(9)
h.display_info()
h.fire_alarm()


building = Building(0,20,5)
building.run_elevator(1,6)
building.run_elevator(3,2)
building.run_elevator(2,4)
