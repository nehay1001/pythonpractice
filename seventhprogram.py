#let practice i/o file in python
# creat a new file "practice.txt" using python.add the following data in it:
# hi everyone
# we are learning file I/o
# using java.
# i like programming in java.

with open("practice.txt","w") as f:
    f.write("hi everyone\nwe are learning file I/o\n")
    f.write("using java.\ni like programming in java.")


# WAF that replace all occurrences of "java" with "python" in above file.
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


# search if the word "learning" exists in the file or not.
word="learning"
with open ("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")


word="xlearning"
with open ("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")


def check_for_word(): # if we solve using function
 word="xlearning"
 with open ("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1): # we can also write here f(word in data):
        print("found")
    else:
        print("not found")
check_for_word()

 
# WAF to find in wich line of the file does the word "learning" occur first.
# print -1 if word not found
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f :
        while  data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1
check_for_line()


def check_for_line():
    word="programming"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1
check_for_line()


def check_for_line():
    word="pyq"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1
print(check_for_line())



#from a file containing number seprated by comma, print the count of even numbers.
with open("practices.txt","r") as f:
    data=f.read()
    print(data)

    num=""
    for i in range(len(data)):
        if(data[i]== ","):
            print(int(num))
            num= ""
        else:
            num +=data[i]



with open("practices.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    print(nums)


count=0
with open("practices.txt","r") as f:
    data=f.read()
    
    nums=data.split(",")
    for val in nums:
        if(int(val) % 2 ==0):
            count +=1

print(count)
    