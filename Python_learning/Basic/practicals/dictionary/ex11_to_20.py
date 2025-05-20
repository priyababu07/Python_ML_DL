#11
thisdict = {}
input ="haihello"
for x in input:
    if x in thisdict:
        thisdict[x]=thisdict[x]+1
    else:
        thisdict[x]=1
print(thisdict)

#12

cities = {
    'Mumbai': 20,
    'Delhi': 16,
    'Bangalore': 84,
    'Hyderabad': 68,
    'Chennai': 70
}
larg = 0
val = ""
for x, y in cities.items():
    if y > larg:
        larg = y
        val = x

print(val, larg)

#13
students = {
    'Alice': 88,
    'Bob': 95,
    'Charlie': 67,
    'David': 76,
    'Eva': 90
}
larg = 0
val = ""
for x, y in students.items():
    if y > larg:
        larg = y
        val = x

print(val, larg)

#14
sortedkeys = dict(sorted(cities.items()))
print(sortedkeys)

#15
sorted_by_values = sorted(cities.keys())
print("Sorted by values:", sorted_by_values)




#16
sq={}
for x in range(1,7):
   sq[x] = x**2
print(sq)





#17
keys = ['name', 'age', 'gender']
values = ['Alice', 25, 'Female']

combined_dict = dict(zip(keys, values))
print("Combined dictionary:", combined_dict)

#18
colors = {
    'John': 'Blue',
    'Alice': 'Green',
    'Bob': 'Blue',
    'Eve': 'Red',
    'Charlie': 'Green'
}

unique_colors = {}
seen = set()

for key, value in colors.items():
    if value not in seen:
        unique_colors[key] = value
        seen.add(value)

print("Dictionary with unique values:", unique_colors)

#19
def check_or_add(d, key, default_value):
    if key in d:
        return "Key exists"
    else:
        d[key] = default_value
        return f"Key added with default value: {default_value}"

my_dict = {'x': 10, 'y': 20}
print(check_or_add(my_dict, 'z', 0))
print("Updated dictionary:", my_dict)

#20
people = {
    'Alice': 28,
    'Bob': 35,
    'Charlie': 40,
    'David': 25,
    'Eve': 32
}

print("People older than 30:")
for name, age in people.items():
    if age > 30:
        print(name)
