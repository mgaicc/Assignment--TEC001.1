import random
class Car:
    def __init__(self, regisnations_number:str, maximun_speed :int):
        self.regisnations_number = regisnations_number
        self.maximun_speed = maximun_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self,change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximun_speed:
            self.current_speed = self.maximun_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hour):
        self.hour = hour
        self.travelled_distance = (self.hour * self.current_speed) + self.travelled_distance
    def __str__(self):
        return f'The regisnations plates is {self.regisnations_number}.\nThe maximun speed is {self.maximun_speed} km/h'
class Race:
    def __init__(self,name:str,distance_in_kilometers:float,list_cars:list):
        self.name = name
        self.distance_in_kilometers = distance_in_kilometers
        self.list_car = list_cars
        self.hour = 0
    def hour_passes(self):
        self.hour += 1
        for car in self.list_car:
            speed_change = random.randint(-10,15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print(f'\n Hour: {self.hour}')
        print(f"{'Reg Number':<10}| {'Max Speed':<10}| {'Speed':<10}| {'Distance':<15}")
        print("-" * 50)
        for car in self.list_car:
            print(f'{car.regisnations_number:<10}'
                f'{car.maximun_speed:<10}'
                f'{car.current_speed:<10}'
                f'{car.travelled_distance:<15.2f}')
        return
    def race_finished(self):
        for car in self.list_car:
            if car.travelled_distance >= self.distance_in_kilometers:
                return True
        return False

    

#Main program
car_storage = []
for i in range(1,11):
    car_speed = random.randint(150,200)
    car_name = f'ABC-{i}'   
    car_storage.append(Car(car_name,car_speed))
race = Race('Grand Demolition Derby',8000,car_storage)
while not race.race_finished():
    race.hour_passes()
    if race.hour % 10 == 0:
        race.print_status()
race.print_status()
