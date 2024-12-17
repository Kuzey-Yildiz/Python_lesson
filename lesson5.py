# dictionaries

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(mydict)
print(mydict["model"])
print(mydict["year"])

# A dictionary is a collection which is ordered*,
# changeable and do not allow duplicates.

# Dictionaries are changeable, meaning that we can change, add or
# remove items after the dictionary has been created.

print(len(mydict))

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

type(thisdict)

# constructors
list()
tuple()
set()
dict()

# get()
mydict = {
    "name": "Abdurrahman",
    "surname": "Karaca",
    "hometown": "Erzurum",
    "school": "İstanbul Kültür Üniversity",
    "pets": "None"
}

a = mydict.get("name")
a

# keys()
a = mydict.keys()
print(a)


# values()
b = mydict.values()
b


mydict["school"] = "marmara"
mydict

# items()
x = mydict.items()

# if key exist
mydict = {
    "name": "Abdurrahman",
    "surname": "Karaca",
    "hometown": "Erzurum",
    "school": "İstanbul Kültür Üniversity",
    "pets": "None"
}

if "school" in mydict:
    print("yes")

# update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
thisdict

thisdict.update({"engine": "V8"})
thisdict

# removing
# pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# you can delete specific item
thisdict.pop("model")
print(thisdict)

# popitem()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)

# clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
print(thisdict)

# loops
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# keys
for x in thisdict:
    print(x)

for x in thisdict.keys():
    print(x)

# values
for x in thisdict.values():
    print(x)

for x in thisdict:
    print(thisdict[x])


for x, y in thisdict.items():
  print(x, y)

# copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict)

# dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# nested dic.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three dictionaries, then create one dictionary
# that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


print(myfamily["child1"]["name"])
print(myfamily["child1"]["year"])

# loop through nested dic.
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


for y in obj:
    print(y + ':', obj[y])