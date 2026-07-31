age=21
if(age >= 18):
    print("i can drive and apply for license")

age=24
if(True):
    print("can drive")
    print("can vote")

light="green"
if(light=="red"):
    print("stop")
if(light=="green"):
    print("go")
if(light=="yellow"):
    print("look")

print("end of code")


num=5
if(num>2):
    print("num greater then 2")
if(num>3):
    print("num greater then 3")

num=5
if(num>2):
    print("num greater then 2")
elif(num>3):
    print("num greater then 3")

light="pink"
if(light=="red"):
    print("stop")
elif (light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")



age=14
if(age>=18):
    print("can vote")#indentation {}
else:
    print("cannot vote")


marks=74
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<=90):
    grade="B"
elif(marks>=70 and marks<=80):
    grade="C"
else:
    grade="D"
