# del key
class Student:
    def __init__(self,name):
         self.name=name

s1=Student("neha")
print(s1)
del s1
# print (s1)  #if we print then error show becoz we use del s1

class Student:
    def __init__(self,name):
         self.name=name

s1=Student("neha")
print(s1.name)
del s1.name
# print (s1.name)  # if we print then error show becoz we use del s1.name