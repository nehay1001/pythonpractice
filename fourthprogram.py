# dictionary in python
inf={
    "key":"value",
    "name":"apnacollege",
    "learning":"python",
    "age":20,
    "is_student":True,
    "marks":92.60,
}

print(inf)


inf={
    
    "name":"apnacollege",
    "subject":["c","python","java"],
    "tuple":("dictionary","list","tuple"),
    "learning":"python",
    "age":20,
    "is_student":True,
    "marks":92.60,
}



print(inf)
print(type(inf))

inf={
    
    "name":"apnacollege",
    "subject":["c","python","java"],
    "tuple":("dictionary","list","tuple"),
    "learning":"python",
    "age":20,
    "is_student":True,
    "marks":92.60,
}

print(inf["name"])
print(inf["subject"])
print(inf["tuple"])
print(inf["learning"])
print(inf["age"])
print(inf["is_student"])
print(inf["marks"])

inf["name"]="nehayadav"#ovewrite or we can put number also
print(inf)

inf["name"]="neha"
inf["surname"]="yadav"
print(inf)

nul_dict={}
print(nul_dict)

nul_dict={}
nul_dict["name"]="neha"
print(nul_dict)


#nested dictionary
student={
        "name":"neha",
        "subject":{
            "physics":90,
            "maths":80,
            "chemistry":70,
        }

}

print(student)
print(student["subject"])
print(student["subject"]["physics"])


#methods in dictionary
inf={
    "name":"apnacollege",
    "subject":["c","python","java"],
    "tuple":("dictionary","list","tuple"),
    "learning":"python",
    "age":20,
    "is_student":True,
    "marks":92.60,
}
print(inf.keys())# inf.key()
print(list(inf.keys()))
print(len(list(inf.keys())))
print(len(inf))

print(inf.values())# inf.values()
print(list(inf.values()))
print(len(list(inf.values())))
print(len(inf))


print(inf.items())# inf.items()
print(list(inf.items()))
pairs=list(inf.items())
print(pairs[0])
print(pairs[1])

print(inf.get("name"))# inf.get("name")
print(inf["name"])# inf["name"]

print(inf.get("name2"))# not error-> none
print(inf["name2"])#error

print("BEFORE")
print(inf["name2"])#error
print("AFTER")

student.update({"city":"delhi"})
print(student)

new_dict={"city":"delhi",}
student.update(new_dict)
print(student)


new_dict={"city":"delhi","age":"20",}
student.update(new_dict)
print(student)

new_dict={"name":"yadav",}
student.update(new_dict)
print(student)
