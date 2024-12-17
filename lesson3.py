# loop list

mylist = ["Abdurrahman", "Ömer", "Ozan", "Ege"]

for x in mylist:
    print(x)

# range(), len()
for i in range(len(mylist)):
    print(mylist[i])

# range(), len()
for i in range(1,2):
    print(mylist[i])

# while loop
mylist = ["Abdurrahman", "Ömer", "Ozan", "Ege"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

######################
# list comprehension
######################
mylist = ["Abdurrahman", "Ömer", "Ozan", "Ege"]
[print(x) for x in mylist]

# example
mylist = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
newlist = []

for x in mylist:
    if "a" in x:
        newlist.append(x)

print(newlist)

# list comprehension example
mylist = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
newlist = [x for x in mylist if "a" in x]
print(newlist)

# != not kemal
mylist = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
newlist = [x for x in mylist if x != "Kemal"]
print(newlist)

# iterable - range()
newlist = []
newlist = [x for x in range(9)]
print(newlist)

newlist = []
newlist = [x for x in range(1, 7)]
print(newlist)

# example
newlist = [x for x in range(10) if x < 5]
print(newlist)

mylist = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
newlist = [x.upper() for x in mylist]
print(newlist)

mylist = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
newlist = [x.capitalize() for x in mylist]
print(newlist)

# example
fruits = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
newlist = [x if x != "Pineapple" else "Orange" for x in fruits]
print(newlist)

# sort list - alphabetically
fruits = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
fruits.sort()
print(fruits)

# sort numbers
numbers = [5, 2, 1, 4, 3]
numbers.sort()
print(numbers)

# sort descending
fruits = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
fruits.sort(reverse = True)
print(fruits)

# sort numbers
numbers = [5, 6, 2, 1, 4, 3]
numbers.sort(reverse = True)
print(numbers)

# case insensitive sort
# sort method is case sensitive
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
thislist.sort()
print(thislist)

# perform a case-insensitive sort of the list
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
thislist.sort(key = str.lower)
print(thislist)

# copy a list
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
mylist = thislist.copy()
print(mylist)

# another way to make a copy is to use list() method
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
mylist = list(thislist)
print(mylist)

# example
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
mylist = thislist[:3]
print(mylist)

# python join list
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
numbers = [3, 6, 4, 1, 2, 5]
list3 = thislist + numbers
print(list3)

# append() method
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
numbers = [5, 4, 1, 2, 6, 3]

for x in numbers:
    thislist.append(x)

print(thislist)

# extend()
thislist = ["Banana", "Kiwi", "Cheery", "Peanut", "Pineapple"]
numbers = [5, 6, 2, 1, 4, 3]

thislist.extend(numbers)
print(thislist)