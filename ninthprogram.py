# let's practice
 
# Qs1. define a circle class to creat circle with radius r using the constructor.
# define an area () method of class which calculatethe area of the circle.
# define a perimeter () method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius **2

    def perimeter(self):
        return 2 * (22/7) *self.radius

c1=Circle(21)
print(c1.area())
print(c1.perimeter())



# Qs2. define a Employee class with attributes role .department and salary.this class also have showDetails() method.
     # creat an engineer class that inherits properties from employee and has additional attributes : name and age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

e1=Employee("accountant","Finance","60,000")
e1.showDetails()



class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")

engg1=Engineer("Elon Musk",40)
engg1.showDetails()




# creat class called order which store item and its price.    use Dunder function _ _ gt _ _() to convey that:
# order1>order2 if price of order1 >price of order 2

class Order:
    def __init__(self,item, price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1=Order("chips",20)
odr2=Order("tea",15)

print(odr1 > odr2)   # true