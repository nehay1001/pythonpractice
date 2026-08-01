#practice
#WAP to ask the user to enter a names of their three favourite movie and store them in a list .
movie1=input("Enter your first favourite movie: ")
movie2=input("Enter your second favourite movie: ")
movie3=input("Enter your third favourite movie: ") 
list=[movie1,movie2,movie3]
print("your favourite  movies are:",list)

### OR
movies=[]
movie1=input("Enter your first favourite movie: ") #we can also use append in next line.
movie2=input("Enter your second favourite movie: ")
movie3=input("Enter your third favourite movie: ") 

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


#WAP to check if list contain a palidrome of element .( hint:use copy () methode)
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if (copy_list1==list1):
    print(" palindrome")
else:
    print("not palindrome")


list1=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if (copy_list1==list1):
    print(" palindrome")
else:
    print("not palindrome")



#WAP to count the number of student with the "A" grade in the following tuple
grade=("A","B","C","D","A","B","C","D","A")
print(grade.count("A"))



#store the above value in list and sort them from "A" to "D"
list=["A","B","C","D","A","B","C","D","A"]
list.sort()
print(list) 