#set in python 
collection={1,2,3,4}
print(collection)
print(type(collection))

collection={1,2,2,2,"hello","world","world"}
print(collection)

collection={1,2,2,2,"hello","world","world",4}
print(collection)
print(len(collection))

collection={}  #but this is empty dictinory
print(type(collection))

collection=set() #empty set: syntax
print(type(collection))

#set methode
collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("nehayadav")
collection.add((1,2,3,))
print(collection)
print(len(collection))

collection.remove(1)
collection.remove(2)
print(collection)

collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("nehayadav")
collection.add((1,2,3,))

collection.clear()
print(collection)
print(len(collection))

collection={"hello","apnacollege","world","coding","python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())

set1={1,2,3,}
set2={2,3,4,}
print(set1.union(set2)) #{1,2,3,4}
print(set1)
print(set2)

set1={1,2,3,}
set2={2,3,4,}
print(set1.intersection(set2)) #{2,3}
print(set1)
print(set2)
