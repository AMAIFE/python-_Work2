
import abc


def drive_direction():
    pass


class Vehicle:

    @abc.abstractmethod
    def get_name(self):
        pass


class Car(Vehicle):
    def get_name(self):
        print("drive_forward")


class Plane(Vehicle):
    def get_name(self):
        print("drive_upward")


car = Car()
car.get_name()

plane = Plane()
plane.get_name()






