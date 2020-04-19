import threading
import time

def menu(cars):
    m = '''\nWelcome to the car Program!
    1. Create Car
    2. Accelerate Car
    3. Brake Car
    4. Run Car (Running on thread)
    5. Display Cars\n'''
    while True:
        print(m)
        option = input('Select option: ')
        if option == '1':
            name = add_car()
            car = Car(name)
            cars.append(car)
        elif option == '2':
            choice = select_car(cars)
            cars[int(choice)].accelerate()
        elif option == '3':
            choice = select_car(cars)
            cars[int(choice)].start_braking()
        # elif option == '4':
        #     choice = select_car(cars)
        #     cars[int(choice)].run()
        elif option == '5':
            disp_cars(cars)

def add_car():
    name = input('Enter car name: ')
    return name

def disp_cars(cars):
    for i, car in enumerate(cars):
        # print('\n({0}) {1}'.format(i, car.name))
        print('Car {0} is traveling at a speed of {1}m/s and has traveled a distance of {2}m'.format(car.name, car.speed, car.dist))

def select_car(cars):
    for i, car in enumerate(cars):
        print('\n({0}) {1}'.format(i, car.name))
    choice = input('\nSelect Car: ')
    return choice

class Car(object):
    def __init__(self, name='Generic Car Name', interval=1):
        self.name = name
        self.dist = 0
        self.speed = 0
        self.accel = 0
        self.brake_accel = 2
        self.cit = 1
        self.interval = 1
        self.is_running = True
        self.braking = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def accelerate(self):
        if self.braking == True:
            self.braking = False
        self.accel += 1
        # self.dist = self.dist + (self.speed*self.cit) + (self.accel*self.cit**2/2)
        self.speed = self.speed + (self.accel*self.cit)
        #print('The car is traveling at a speed of {0}m/s and has traveled a distance of {1}m'.format(self.speed, self.dist))

    def start_braking(self):
        self.braking = True

    def brake(self):
        self.accel -= self.brake_accel
        if self.speed <= 0:
            self.accel = 0
            self.speed = 0
            self.braking = False
            print('Car has come to a halt.')
        elif self.accel > 0:
            self.dist = self.dist + (self.speed*self.cit) - (self.brake_accel*self.cit**2/2)
            self.speed = self.speed - (self.brake_accel*self.cit)
        elif self.accel <= 0:
            self.accel = 0
            self.dist = self.dist + (self.speed*self.cit) - (self.brake_accel*self.cit**2/2)
            self.speed = self.speed - (self.brake_accel*self.cit)


        #print('The car is traveling at a speed of {0}m/s and has traveled a distance of {1}m'.format(self.speed, self.dist))

    def run(self):
        while True:
            if self.braking == True:
                while self.speed != 0:
                    self.brake()
                    time.sleep(self.interval)
            self.dist = self.dist + (self.speed*self.cit) + (self.accel*self.cit**2/2)
            self.speed = self.speed + (self.accel*self.cit)*0.5
            #print('The car is traveling at a speed of {0}m/s and has traveled a distance of {1}m'.format(self.speed, self.dist))
            time.sleep(self.interval)


def main():
    cars = []
    menu(cars)

main()