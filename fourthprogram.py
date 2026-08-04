# practice5
# store following word meaning in python dictonary
#  (table:"a piece of furniture","list of facts and figure"
#   cat:"a small animals")

dict={ 
      "table":["a small piece of furniture","list of fact and figure"],
      "cat" : "a small animals"
} 

print(dict)

# you are giving a list of subject of student .assume one classroom is required for 1 subject,how many classroom are needed by all student.
# ("python","java","c++","python","javascript","java","python","java","c++","c")

subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(subject)
print(len (subject))


# WAP to enter the marks of three subject from the user and store in dictonary .start with an empty dictonary and add one by one .use subject name as a key and marks as value
marks={}
x=int(input("enter phy :"))
marks.update({"phy":x})

x=int(input("enter maths :"))
marks.update({"maths":x})

x=int(input("enter chem :"))
marks.update({"chem":x})

print(marks)


#figure out a way to store 9 and 9.0 as separate value in the set.(you can take help of built in data type)
value={9,"9.0"}
print(value)

value={
    ("float",9.0),
    ("int",9)
}

print(value)