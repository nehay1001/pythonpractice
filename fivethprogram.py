#loops in python 
# for loops 
nums=[1,2,3,4,5]
for value in nums:
    print(value)

veggies=["potato","brinjal","lady finger","cucumber"]
for value in veggies:
    print(value) 

tup=(1,2,3,4,5,8,6)
for nums in tup:
    print(nums)

str="apnacollege"
for char in str:
    print(char)

str="apnacollege"
for char in str:
    print(char)
else:
    print("END")


str="apnacollege"
for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("END")


str="apnacollege"
for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
print("END")


## practice

    

#print the elements of the following list using loops.[1,4,9,16,25,36,49,64,81,100]

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums :
    print(el)


#search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100,49)
nums=(1,4,9,16,25,36,49,64,81,100,49)

x=49

indx=0
for el in nums:
    if(el==x):
        print("numbers found at indx",indx)
    indx+=1


nums=(1,4,9,16,25,36,49,64,81,100,49)

x=49

indx=0
for el in nums:
    if(el==x):
        print("numbers found at indx",indx)
        break
    indx+=1
    
    