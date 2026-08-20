class Bird:
    def fly(self):
        print("Bird is flying")


class Airplane:
    def fly(self):
        print("Airplane is flying")


class Drone:
    def fly(self):
        print("Drone is flying")


def make_fly(obj):
    obj.fly()


bird = Bird()
airplane = Airplane()
drone = Drone()

make_fly(bird)
make_fly(airplane)
make_fly(drone)