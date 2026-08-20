f=open("demo.txt","w")
f.write("my fav player abhishek sharma.")
f.close()

f=open("demo.txt","a")
f.write(" my fav singer zany malik")
f.write("\n i am girl")
f.close()

f=open("sample.txt","w")
f.close()

f=open("samp.txt","a")
f.close()

f=open("demo.txt","r+")
f.write("abc")
f.close()

f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

f=open("demo.txt","w+")
#f.write("abc")
print(f.read())
f.write("abc")
f.close()

f=open("demo.txt","a+")
#f.write("abc")
print(f.read())
f.write("abc")
f.close()
