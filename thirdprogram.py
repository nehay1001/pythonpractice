#python tuple
tup=(1,2,3,4,5)# if want to add , is also possible 
print(type(tup))
print(tup[0])
print(tup[2])
tup[0]=10 #tuple is immutable

tup=()
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))

tup=(1)
print(tup)
print(type(tup))

tup=(1.0)
print(tup)
print(type(tup))

tup=("hello",)
print(tup)
print(type(tup))

tup=("hello",)
print(tup)
print(type(tup))

#slicing in tuple
tup=(1,2,3,4,5)
print(tup[1:4])
print(tup[:3])
print(tup[2:5])

#tuple methods
tup=(1,2,3,4,5,)
print(tup.index(3))
print(tup.count(3))
