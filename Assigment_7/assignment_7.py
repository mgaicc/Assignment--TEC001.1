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
new_car = Car('ABC-123',142)
print(new_car)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f'After accelerations. Current Speed {new_car.current_speed}')
new_car.drive(1.5)
print(f'Total travelled distance {new_car.travelled_distance}')
new_car.accelerate(-200)
print(f'After slow down. Current Speed {new_car.current_speed}')

import random
car_storage = []
for i in range(1,11):
    car_speed = random.randint(150,200)
    car_name = f'ABC-{i}'
    car_storage.append(Car(car_name,car_speed))
race = False
hour_passed = 0
while not race:
    hour_passed += 1
    for car in car_storage:
        speed_change = random.randint(-10,15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race = True
print("\nRace Results:")
print(f"{'Reg Number':<10}| {'Max Speed':<10}| {'Speed':<10}| {'Distance':<15}")
print("-" * 50)

for car in car_storage:
    print(f'{car.regisnations_number:<10}'
          f'{car.maximun_speed:<10}'
          f'{car.current_speed:<10}'
          f'{car.travelled_distance:<15.2f}')
