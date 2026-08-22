class Account:                               #for public
    def __init__ (self,acc_no,acc_pass):   
        self.acc_no=acc_no
        self.acc_pass=acc_pass

acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.acc_pass)

#class Account:                               #for private 
    #def __init__ (self,acc_no,acc_pass):
        #self.acc_no=acc_no
        #self.__acc_pass=acc_pass

#acc1=Account("12345","abcde")
#print(acc1.acc_no)
#print(acc1.__acc_pass)                       # give error

class Account:                               #for private 
    def __init__ (self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(acc1.__acc_pass)

acc1=Account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass())


#class Person:                       # its private (__) that's why give error
   # __name="anonymous"
#p1=Person()
#print(p1.__name)


#class Person:                       # its private (__)that's why give error
    #__name="anonymous"

    #def __hello():
       # print("hello person!")

#p1=Person()
#print(p1.__hello())

class Person:                       
    __name="anonymous"

    def __hello(self):
       print("hello person!")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())

