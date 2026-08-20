f=open("demo.txt","r") 
data=f.read()
print(data)
print(type(data))
f.close()

f=open("demo.txt","r")
data=f.read(5)
print(data)
f.close()


f=open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()


f=open("demo.txt","r")
data=f.read()
print(data)
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()


f=open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()