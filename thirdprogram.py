
student=["radhika",45.67,12,"mumbai"]# this onlu in list not in string
print(student[0])
student[0]="priyanshi"
print(student)

student==["radhika",45.67,12,"mumbai"]
print(student[3])


#list slicing
marks=[45,67,89,90,78,56]
print(marks[1:5])#1 to 4 index value
print(marks[1:])#1 to last index value
print(marks[:5])#0 to 4 index value
print(marks[:])#0 to last index value
print(marks[-5:-1])#-5 to -2 index value
print(marks[-5:-3])#-5 to -4 index value