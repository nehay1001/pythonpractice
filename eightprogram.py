# static method

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod   # static method
    def hello():
        print("hello")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)

s1=Student("tony shark",[98,97,96])
s1.get_avg()
s1.hello()


# abstraction
class Car:

    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False


    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")


car1=Car()
car1.start()


#let's practice
# creat account class with 2 attributes-balance and account no.
# creat method for debit(-ve) , credit(+ve) and print the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)



class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    # debit method
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
            self.balance +=amount
            print("Rs.",amount,"was credited")
            print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)



class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    # debit method
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
            self.balance +=amount
            print("Rs.",amount,"was credited")
            print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)