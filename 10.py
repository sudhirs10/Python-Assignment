# 1
# Elevator program
# Moves up and down between floors
# starts from the bottom floor and moves to top
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.current_floor = bottom_floor
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor = self.current_floor + 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At top floor")
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor = self.current_floor - 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At bottom floor")
#     def go_to_floor(self, target_floor):
#         print("Move to floor", target_floor)
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#         print("Now at floor", self.current_floor)
# elevator = Elevator(1, 10)
# elevator.go_to_floor(5)
# print()
# elevator.go_to_floor(1)

# 2
# Elevator and Building program
# building has elevators that move between floors

# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.current_floor = bottom_floor
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor = self.current_floor + 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At top floor")
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor = self.current_floor - 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At bottom floor")
#     def go_to_floor(self, target_floor):
#         print("Move to floor", target_floor)
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#         print("Now at floor", self.current_floor)
# class Building:
#     def __init__(self, bottom_floor, top_floor, num_elevators):
#         self.elevators = []
#         count = 0
#         while count < num_elevators:
#             new_elevator = Elevator(bottom_floor, top_floor)   # created one elevator
#             self.elevators.append(new_elevator)                 # addingto the list
#             count = count + 1
#         print("Building created with", num_elevators, "elevators from floor", bottom_floor, "to", top_floor)
#     def run_elevator(self, elevator_number, target_floor):
#         print("Elevator", elevator_number + 1, "is starting to floor", target_floor)
#         chosen_elevator = self.elevators[elevator_number]
#         chosen_elevator.go_to_floor(target_floor)
#         print("Elevator", elevator_number + 1, "has reached floor", target_floor, "and stopped")
# my_building = Building(1, 10, 3)
# my_building.run_elevator(0, 5)
# my_building.run_elevator(1, 8)
# my_building.run_elevator(2, 3)

# 3
# Elevator and Building program with Fire Alarm
# building has elevators that move between floors
# When fire alarm rings all elevators go to the bottom floor

# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.current_floor = bottom_floor
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor = self.current_floor + 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At top floor")
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor = self.current_floor - 1
#             print("Elevator on floor", self.current_floor)
#         else:
#             print("At bottom floor")
#     def go_to_floor(self, target_floor):
#         print("Move to floor", target_floor)
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#         print("Now at floor", self.current_floor)
# class Building:
#     def __init__(self, bottom_floor, top_floor, num_elevators):
#         self.elevators = []
#         count = 0
#         while count < num_elevators:
#             new_elevator = Elevator(bottom_floor, top_floor)
#             self.elevators.append(new_elevator)
#             count = count + 1
#         print("Building created with", num_elevators, "elevators from floor", bottom_floor, "to", top_floor)
#     def run_elevator(self, elevator_number, target_floor):
#         print("Elevator", elevator_number + 1, "is starting to floor", target_floor)
#         chosen_elevator = self.elevators[elevator_number]
#         chosen_elevator.go_to_floor(target_floor)
#         print("Elevator", elevator_number + 1, "has reached floor", target_floor, "and stopped")
#     def fire_alarm(self):
#         print()
#         print("Fire alarm has started in building.")
#         print("All elevators will go down to the bottom floor.")
#         elevator_num = 1
#         for elevator in self.elevators:
#             print()
#             print("Elevator", elevator_num, "was on floor", elevator.current_floor)
#             print("Moving Elevator", elevator_num, "to the bottom floor...")
#             elevator.go_to_floor(elevator.bottom_floor)
#             print("Elevator", elevator_num, "is now at the bottom floor.")
#             elevator_num = elevator_num + 1
#         print()
#         print("All elevators are now at the bottom floor.")
#         print("Fire alarm process is completed.")
# my_building = Building(1, 10, 3)
# my_building.run_elevator(0, 5)
# my_building.run_elevator(1, 8)
# my_building.run_elevator(2, 3)
# my_building.fire_alarm()


# 4
# Program creates a car race simulation
# Each car has a registration number, max speed, current speed, and travelled distance
# Cars change speed randomly and move every hour
# The race ends when one of the cars reaches 8000 km

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
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)  
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print("---- Current race situation ----")
        print("Details of all cars:")
        for car in self.cars:
            print("Car", car.registration_number, "has travelled", int(car.travelled_distance),"kilometers and it is moving at", car.current_speed, "km/h.")
        print("End of status update.\n")

    def race_finished(self):
        finished = False
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                finished = True
        return finished
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    reg = "ABC-" + str(i)
    car = Car(reg, max_speed)
    car.current_speed = car.max_speed
    cars.append(car)
race = Race("Grand Demolition Derby", 8000, cars)
print("A new race ", race.name, "has started with a distance of", race.distance_km, "kilometers.")
hours = 0
while race.race_finished() == False:
    hours = hours + 1
    race.hour_passes()
    if hours % 10 == 0:
        print("After", hours, "hours of racing, this is the current situation:")
        race.print_status()
print("Race has finished after", hours, "hours.")
race.print_status()
print("The event", race.name, "has now ended. Thank you!")



