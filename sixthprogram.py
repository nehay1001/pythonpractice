#function in python
def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(4,8)

def calc_sum(a,b):
   return a+b
sum=calc_sum(3,4)
print(sum)

def calc_diff(a,b,):
    diff=a-b
    print(diff)
calc_diff(9,5,)

def calc_multi (a,b):
    return a*b
multi=calc_multi(4,4)
print(multi)

def cal_div(a,b):
    div=a/b
    print(div)
cal_div(5,2)

def cal_mod(a,b):
    return a%b
mod=cal_mod(4,4)
print(mod)

def cal_pow(a,b):
    return a**b
pow=cal_pow(5,2)
print(pow)


def print_hello():
        print("hello")
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


print_hello()
print("hello")

output=print_hello()
print(output) ## none

def print_neha():
    print("neha")
print_neha()

#avarage of 3 function
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg (1,2,3)

def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg (98,97,95)


#buil in function #1.print() 2.len()  3.type()  4.range()

print("helloworld","nehayadav") #sep=""
print("helloworld") #sep=""
print("nehayadav") #end="\n"

print("helloworld",end="")
print("nehayadav")

print("helloworld",end="$")
print("nehayadav")

# defalt parameter

def calc_multi(a=4,b=2):
    print(a*b)
    return a*b

calc_multi()

def calc_multi(a,b=2): #first use non defalt then defalt
    print(a*b)
    return a*b

calc_multi(4)


#WAF to print the length of list.( list is the parameter )

cities=["mumbai","andheri","malad","bandra","marol","pune","delhi"]
heroes=["batman","thor","captain america","saktiman","'spiderman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# WAF to print the element of a list in a single line.( list is the parameter)

cities=["mumbai","andheri","malad","bandra","marol","pune","delhi"]
heroes=["batman","thor","captain america","saktiman","'spiderman"]

print(heroes[0], end=" ")
print(heroes[1], end=" ")

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

cities=["mumbai","andheri","malad","bandra","marol","pune","delhi"]
heroes=["batman","thor","captain america","saktiman","'spiderman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)
print()
print_list(cities)
print()



#WAP to find the factorial of n.(n is the parameter).
n=5
fact=1
for i in range(1,n+1):
    fact*=i 
print(fact) #this is we read in loops 

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
     fact*=i 
    print(fact) 

cal_fact(5)
cal_fact(4)


#WAF to convert USD to INR
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =" ,inr_val,"INR")

converter(1)
converter(100)
converter(73)