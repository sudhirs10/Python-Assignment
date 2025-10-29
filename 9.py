# 1
# Creates a car with speed and distance set to 0
# Prints all car details
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
my_car = Car("AB-123", 142)
print(f"Registration number of Car is {my_car.registration_number}: The Max speed of car is {my_car.max_speed} km/h, current speed is{my_car.current_speed} km/h and the travelled distance is {my_car.travelled_distance} km")

# 2
# Adding accelerate method to change car speed
# Tests with +30, +70, +50 and then -200 for braking
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
my_car = Car("AB-123", 142)
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"The current speed is: {my_car.current_speed} km/h")
my_car.accelerate(-200)
print(f"The final speed after braking is : {my_car.current_speed} km/h")


# 3
# Adding drive method to calculate distance using time and speed
# Then prints all car detail
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours
my_car = Car("AB-123", 142)
my_car.accelerate(60)
my_car.drive(1.5)
print("Car:", my_car.registration_number)
print("Max speed of Car:", my_car.max_speed, "km/h")
print("Current speed of Car:", my_car.current_speed, "km/h")
print("Total Travelled distance:", my_car.travelled_distance, "km")

# 4
# make 10 cars and starts a race
# speed changes every hour
# race ends when one car reaches 10000 km
# Car Race Program
# This program creates 10 cars and makes them race until one travels 10,000 km

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours
cars = []
for i in range(1, 11):
    speed = random.randint(100, 200)
    reg = "ABC-" + str(i)
    car = Car(reg, speed)
    cars.append(car)
race_over = False
hours = 0
print("The race has started!")
while race_over == False:
    hours = hours + 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        time = 1
        car.drive(time)
        if car.travelled_distance >= 10000:
            race_over = True
            break
print()
print("Race finished after", hours, "hours.")
print("Car details:")
print("Registration Number", "----MaxSpeed", "----CurrentSpeed", "----Distance")
for car in cars:
    print(car.registration_number, car.max_speed, car.current_speed, car.travelled_distance)




