# recursion in python
def show(n):
    print(n)
show(7)

def show(n):
    print(n)
show(6)

def show(n):
    print(n)
show(5) #5=n,4=n-1,3=n-2,2=n-3,1=n-4


# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5) 

def show (n):
    if (n==-1):
        return
    print(n)
    show(n-1)
show(5)

def show(n):
    if(n==0):         # values put here a=123
        return
    print(n)
    show(n-1)
    print("end")
show(3) 


def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1) *n
print (fact(2))


def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1) *n
print (fact(3))

def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1) *n
print (fact(4))


def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1) *n
print (fact(5))


# lest practice
# write a recursive function to calculate the sum of the first n natural numbers.
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)


def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(10)
print(sum)


# write a recursive function to print all elements in list.
#hint: use list and index as parameter
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","lichi","apple","banana"]
print_list(fruits)