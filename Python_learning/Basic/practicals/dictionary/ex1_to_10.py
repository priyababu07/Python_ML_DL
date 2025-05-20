thisdict = {"Title":"Atomic Habit",
            "Author":"Priya",
            "Price":2000}
print(thisdict)
print(thisdict["Title"])

thisdict["year"]=2020
print(thisdict)

thisdict["Author"]="Don"
print(thisdict)

thisdict.pop("year")
print(thisdict)

for i in thisdict:
    if "Title" == i:
        print("Value Exist")

#Dictionary of three students

students = {"stu1":{
    "mark1":20,
    "mark2":30

},
"stu2":{
    "mark1":25,
    "mark2":35

},
"stu3":{
    "mark1":35,
    "mark2":35

}

}
for x in students.values():
    print(x)


thisdict2 = thisdict | students
print(thisdict2)

for x,y in thisdict2.items():
    print(x,y)