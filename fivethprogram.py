# pass staement in loops
for i in range(5):
    pass
print("some useful work")

for i in range(5):
    pass

if i>5:
    pass
print("some useful work")

# practice 
# WAP to find the sum of first n numbers.(using while)
n=5

sum=0
for i in range(1,n+1):
    print(i)
    sum+=i
print("total sum=",sum)  #or

n=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1

print("total sum=",sum) 



#WAP to find the factorial of first n numbers.(using for)
n=3
fact=1
i=1
while i<=n:
    fact*=i
    i+=1

print("factorial=",fact)


n=5
fact=1
for i in range (1,n+1):

    fact*=i
    

print("factorial=",fact)
