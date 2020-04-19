import threading
import time

def menu(cars):
    print('Welcome to the Car Program!\n')
    msg = """What do you want to do?
    1. Create a Car
    2. Accelerate Car
    3. Brake Car
    4. Display Cars
    5. Quit Program."""
    while True:
        print(msg)
        option = input("Select an option: ")
        if option == '1':
            name = input("Enter Car name: ")
            car = Car(name)
            cars.append(car)
        elif option == '2':
            choice = select_car(cars)
            cars[int(choice)].accelerate()
        elif option == '3':
            choice = select_car(cars)
            cars[int(choice)].start_braking()
        elif option == '4':
            disp_cars(cars)
        elif option == '5':
            del cars
            exit(0)
        else:
            print('Invalid Choice')

def disp_cars(cars):
    for i, car in enumerate(cars):
        print("Car {0} is traveling at a speed of {1} and has traveled a distance of {2}m.".format(car.name , car.speed, car.dist))

def select_car(cars):
    for i, car in enumerate(cars):
        print('({0}) {1}'.format(i, car.name))
    option = input('Select a car: ')
    return option
       
class Car(object):
    def __init__(self, name="Fast Car"):
        self.name = name
        self.dist = 0
        self.speed = 0
        self.accel = 0
        self.brake_accel = 5
        self.interval = 1
        self.braking = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    
    def accelerate(self):
        if self.braking == True:
            self.braking = False
        self.accel += 2

    def start_braking(self):
        self.braking = True

    def brake(self):
        self.accel -= self.brake_accel
        if self.speed <= 0:
            self.accel = 0
            self.speed = 0
            self.braking = False
            print('The car has come to a stop.')
        elif self.accel > 0:
            self.dist = self.dist + self.speed*self.interval - self.brake_accel*self.interval**2
            self.speed = self.speed - self.brake_accel*self.interval*0.5
        elif self.accel <= 0:
            self.accel = 0
            self.dist = self.dist + self.speed*self.interval - self.brake_accel*self.interval**2
            self.speed = self.speed - self.brake_accel*self.interval*0.5

    def run(self): # This is our thread
        while True:
            if self.braking == True:
                while self.speed != 0:
                    self.brake()
                    time.sleep(self.interval)
            else:
                self.dist = self.dist + self.speed*self.interval + self.accel*self.interval**2
                self.speed = self.speed + self.accel*self.interval*0.5
                # print("The car has traveled a distance of {}m .".format(self.dist))
                time.sleep(self.interval)

def main():
    cars = []
    menu(cars)

main()