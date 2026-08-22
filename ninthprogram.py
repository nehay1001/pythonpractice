# inheritance
class Car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

print(car1.name)

print(car1.start())              


class Car:

    color="black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

print(car1.color)




class Car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner (ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()



class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)



class Car:

    def __init__(self,type):
            self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super(). __init__(type)

car1=ToyotaCar("prius","electric")
print(car1.type)




class Car:

    def __init__(self,type):
            self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super(). __init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("prius","electric")
print(car1.type)




