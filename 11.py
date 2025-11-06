
class Publication:
    def __init__(self, name):
        self.name = name
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name} - Author: {self.author} - Pages: {self.pages}")
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name} - Chief editor: {self.chief_editor}")
donald_duck = Magazine("Donald Duck", "Aki Hyyppa")
compartment_no6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment_no6.print_information()


#2
class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometers = 0

    def set_speed(self, desired_speed):
        if desired_speed < 0:
            self.current_speed = 0
        elif desired_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = desired_speed

    def drive(self, hours):

        self.kilometers = self.kilometers + self.current_speed * hours
class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_kwh):
        super().__init__(registration, max_speed)
        self.battery_kwh = battery_kwh
class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank_liters):
        super().__init__(registration, max_speed)
        self.tank_liters = tank_liters
ev = ElectricCar("ABC-15", 180, 52.5)
gas = GasolineCar("ACD-123", 165, 32.3)
ev.set_speed(150)
gas.set_speed(140)
ev.drive(3)
gas.drive(3)
print("Electric car", ev.registration, "- kilometers:", ev.kilometers)
print("Gasoline car", gas.registration, "- kilometers:", gas.kilometers)
