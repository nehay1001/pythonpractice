#loops in python

count=1
while count <=5 :
    print("hello")
    count+=1

print(count)

i=1
while i<=5:
    print("apnacollege")
    i+=1
print(i)

i=1
while i<=100:
    print("apnacollege")
    i+=1
print(i)

i=1
while i<=100000:
    print("neha",i)
    i+=1
print(i)

# print number from 1to 5
i=1
while i<=5:
    print(i)
    i+=1

print("loop ended")

# print number from 5 to 1
i=5
while i>=1: # if there i<6 written then loops runs infinite time it can we cras our website
    print(i)
    i-=1

print("loop ended")


#print numbers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1

#print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1

#print the multiplication table of a numbers n.
i=1
while i<=10:
    print(3* i)
    i+=1

n=int(input("enter number:"))
i=1
while i<=10:
    print(n* i)
    i+=1

#print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4]) # print(nums[len(nums)-1]) or

nums=[1,4,9,16,25,36,49,64,81,100]
indx=0
while indx < len(nums):
    print(nums[indx])
    indx+=1

# traverse
heroes=["batman","ironman","thor","superman"]
indx=0
while indx<len(heroes):
    print(heroes[indx])
    indx+=1


#search for a number x in this tuple using loop :(1,4,9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at indx",i)
    i+=1

    

nums=(1,4,9,16,25,36,49,64,81,100)

x=36

i=0
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at indx",i)
    else:
        print("finding..")
    i+=1


nums=(1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at indx",i)
    else:
         print("finding..")
    i+=1