# slicing /negative indexing
str="apple"
print(str[-3:-1])
print(str[-5:-1])
print(str[-5:-2])

#string functions
str="i am studying python from apnacollege"
print(str.endswith("ege"))  #return true if string end with substr
print(str.endswith ("app"))


str="i am studying python from apnacollege"
print(str.capitalize())# capitalized first later
print(str)

print(str.replace("o","a"))#replace all occurance old 
print(str.replace("python","javascript"))

print(str.find("o"))#return 1st index of 1st occurance
str="i am from studing python from apnacollege"
print(str.find("from"))
print(str.find("q"))

str="i am from studying python from apnacollege"
print(str.count("from"))
print(str.count("o"))


#practice
#WAP to input user'first name and print its length
name=input("enter your name:")
print("length of your name is",len(name))

#WAP to find the occurance of $ in a string
str="i have 10$ and this $ i give to how now you count how many $ you have"
print(str.count("$"))



