# class method
class Person:
    name="anonymous"

    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("neha yadav")
print(p1.name)
print(Person.name)



class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name

p1=Person()
p1.changeName("neha yadav")
print(p1.name)
print(Person.name)




class Person:
    name="anonymous"

    def changeName(self,name):
        self.__class__.name="neha"

p1=Person()
p1.changeName("neha yadav")
print(p1.name)
print(Person.name)



class Person:
    name="anonymous"

    #def changeName(self,name):
        #self.__class__.name="neha"

    @ classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("neha yadav")
print(p1.name)
print(Person.name)
