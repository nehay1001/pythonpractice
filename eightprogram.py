class Student:
    name="neha"
s1=Student()
print(s1)


class Student:
    name="neha"
s1=Student()
print(s1.name)


class Student:
    name="neha"
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)


class Car:
    color="blue"
car1=Car()
print(car1.color)


class Car:
    color="blue"
    brand="mercedes"
car1=Car()
print(car1.color)
print(car1.brand)


class Girl:
    look="beautiful"
    height="five feet"
    hair="long"
    eye="black"
    weight="55kg"
    age=20
girl1=Girl()
print(girl1.look)
print(girl1.height)
print(girl1.hair)
print(girl1.eye)
print(girl1.weight)
print(girl1.age)

girl2=Girl()
print(girl2.look)
print(girl2.height)
print(girl2.hair)
print(girl2.eye)
print(girl2.weight)
print(girl2.age)


#__init__function
class Student:
    name="neha"
    def __init__(self):
        print("adding new student in database..")
s1=Student()

class Student:
    name="neha"
    def __init__(self):
        print(self)
        print("adding new student in database..")
s1=Student()
print(s1)


class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database..")
s1=Student("neha")
print(s1.name)
s2=Student("simran")
print(s2.name)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")
s1=Student("neha",98)
print(s1.name,s1.marks)
s2=Student("simran",87)
print(s2.name,s2.marks)

class Student:
#default cons.
    def __init__(self,name,marks):
        pass

#parameterized cons.
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")
s1=Student("neha",98)
print(s1.name,s1.marks)
s2=Student("simran",87)
print(s2.name,s2.marks)


class Student:

    college_name="abc college"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")
s1=Student("neha",98)
print(s1.name,s1.marks)
s2=Student("simran",87)
print(s2.name,s2.marks)

print(s2.college_name) #or
print(Student.college_name)



class Student:

    college_name="abc college"
    name="anonymous" #class attr

    def __init__(self,name,marks):
        self.name=name # obj attr > class attr
        self.marks=marks
        print("adding new student in database..")

s1=Student("neha",98)
print(s1.name)


class Student:

    college_name="abc college"
    
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks

    def welcome(self):
        print("welcome student",self.name)

s1=Student("neha",98)
s1.welcome()



class Student:

    college_name="abc college"
    
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks

s1=Student("neha",98)
s1.welcome()
print(s1. get_marks())


# let's practice
#creat student class that taken name and marks of 3 subject as arguments in constructor. then creat a method to print the avarage.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val

        print("hi",self.name,"your avg score is :",sum/3)


s1=Student("tony shark",[99,98,97])
s1.get_avg()



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is :",sum/3)


s1=Student("tony shark",[99,98,97])
s1.get_avg()

s1.name="ironmen"
s1.get_avg()

