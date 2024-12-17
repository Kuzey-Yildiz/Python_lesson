# tuples
mytuple = ("Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")

# unchangeable
# ordered
# tuples are written with round brackets
# tuple items are indexed, fist index 0, the second index is 1
# allow dublicates

mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple)

# tuple length
print(len(mytuple))

# create tuple with one item
thistuple = ("Abdurrahman",)
print(type(thistuple))

# tuple items can be any data type
# string, int, float, boolean
tuple1 = (True, False, False) # boolean
tuple2 = (4, 5, 6, 7) # int
tuple3 = ("Strawberry", "DragonFruit", "Banana")

# a tuple can contain different data types
tuplelistem = ("Abdurrahman", 72, True, 45, "Kaplumbağa")
print(tuplelistem)
type(tuplelistem)

# tuple() constructor
mytuple = tuple(("Abdurrahman", "Karaca"))
print(mytuple)

# access tuple items
mytuple = ("Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple[3])

# negative index
mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple[-2:])

# range of index
mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple[2:5])

# range of index
mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple[:3])

# range of index
mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
print(mytuple[3:])

# check if item exist
mytuple = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
if "Kiwi" in mytuple:
    print("yes, 'Kiwi' is in the list")

# change tuple items
x = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
type(x) # tuplemış

y = list(x)
type(y)

x = tuple(y)
type(x)

# EXAMPLE
x = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
type(x) # tuple

y = list(x)
y[1] = "Abdurrahman"
x = tuple(y)
type(x)

# add items with append() method
x = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
y = list(x)
y.append("Peanut")
x = tuple(y)

# add tuple to tuple, you are allowed to add tuples to tuples
# tek değerli tuple
x = ("DragonFruit", "Banana")
y = ("Peanut",)
x += y
print(x)

# remove()
x = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
y = list(x)
y.remove("Kiwi")
x = tuple(y)
print(x)
type(x)

# you can delete tuple via del
x = ("Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana")
del x
print(x)

# unpacking tuple
x = ("Apple", "Kiwi", "Cheery")
(Red, Green, Pink) = x
print(Red)
print(Green)
print(Pink)

# using *
x = ("Apple", "Kiwi", "Cheery", "DragonFruit", "Banana")
(red, green, *pink) = x
print(red)
print(green)
print(pink)

# example
x = ("Peanut", "Strawberry", "Apple", "Kiwi", "Cheery", "DragonFruit", "Banana")
(red, *green, pink) = x
print(red)
print(green)
print(pink)

# loops in tuples
mytuple = ("Peanut", "Strawberry", "Apple", "Kiwi", "Cheery", "DragonFruit", "Banana")
for x in mytuple:
    print(x)

# loop through the index numbers
mytuple = ("Peanut", "Strawberry", "Apple", "Kiwi", "Cheery", "DragonFruit", "Banana")
for i in range(len(mytuple)):
    print(mytuple[i])

# example
mytuple = ("Peanut", "Strawberry", "Apple", "Kiwi", "Cheery", "DragonFruit", "Banana")
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
fruits = ("Cheery", "DragonFruit", "Banana")
mytuple = fruits * 2

print(mytuple)

###########
# SET
###########
myset = {"Cheery", "DragonFruit", "Banana"}

#
# Sets are used to store multiple items in a single variable.
#
# Set is one of 4 built-in data types in Python used to store
# collections of data, the other 3 are List, Tuple, and Dictionary,
# all with different qualities and usage.
#
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"Cheery", "DragonFruit", "Banana"}
print(thisset)

# multiline writing shift + option + drag your mouse

#Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them,
# and cannot be referred to by index or key.


# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after
# the set has been created.
# Once a set is created, you cannot change its items,
# but you can remove items and add new items.

# Duplicate values will be ignored:
thisset = {"Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets,
# and are treated as duplicates:

# True and 1 is considered the same value:
thisset = {"Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana", True, 1, 7}
print(thisset)

# False and 0 is considered the same value:
thisset = {"Apple", "Apple", "Kiwi", "Strawberry", "DragonFruit", "Banana", False, True, 0, 1}
print(thisset)

# len()
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
print(len(thisset)

# Set Items - Data Types
# tring, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {19.4, 5.4, 3.3}

# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male", 11.2}
print(set1)

# type()
type(set1)

# set() constructor
# constructor to make a set.
thisset = set(("Kiwi", "Strawberry", "DragonFruit")) # note the double round-brackets
print(thisset)

# list
# ["kemal", "mete", "ege", "rana", "bengisu"]
mynewset = set(["Abdurrahman", "Mete", "Ege", "Rana", "Bengisu"])
print(mynewset)

# Access item
# Loop through the set, and print the values:
thisset = {"Kiwi", "Strawberry", "DragonFruit"}

for x in thisset:
  print(x)

# Check if "Strawberry" is present in the set:
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
print("Strawberry" in thisset)

# Check if "Strawberry" is NOT present in the set:
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
print("Strawberry" not in thisset)

# add()
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
thisset.add("Orange")
print(thisset)

thisset = {"Kiwi", "Strawberry", "DragonFruit"}
thisset.append("Grape") # not working
print(thisset)

# add sets via update() methods  - S
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
tropical = {"Pineapple", "Mango", "Papaya"}
thisset.update(tropical)
print(thisset)

# Remove()
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
thisset.remove("Strawberry")
print(thisset)

# discard() - s
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
thisset.discard("Strawberry")
print(thisset)

# pop()
# Remove a random item by using the pop() method:
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"Kiwi", "Strawberry", "DragonFruit"}
x = thisset.pop()
print(x)
print(thisset)

# clear()
# The clear() method empties the set:
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
thisset.clear()
print(thisset)

# del
# The del keyword will delete the set completely:
thisset = {"Kiwi", "Strawberry", "DragonFruit"}
del thisset
print(thisset)

# loop sets
thisset = {"Kiwi", "Strawberry", "DragonFruit"}

for x in thisset:
  print(x)

# python join sets
# union()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method,
# and you will get the same result.

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"Kiwi", "Strawberry", "DragonFruit"}

myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"Kiwi", "Strawberry", "DragonFruit"}

myset = set1 | set2 | set3 |set4
print(myset)

# join set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"Kiwi", "Strawberry", "DragonFruit"}
set2 = {"Google", "Microsoft", "Amazon"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method,
# and you will get the same result.

set1 = {"Kiwi", "Strawberry", "DragonFruit"}
set2 = {"Google", "Microsoft", "Amazon"}

set3 = set1 & set2
print(set3)

# intersection_update()
# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
set1 = {"Kiwi", "Strawberry", "DragonFruit"}
set2 = {"Google", "Microsoft", "Amazon"}

set1.intersection_update(set2)

print(set1)

# he values True and 1 are considered the same value.
# The same goes for False and 0.

# Join sets that contains the values True, False, 1, and 0,
# and see what is considered as duplicates:
set1 = {"Kiwi", 1,  "DragonFruit", 0, "Strawberry"}
set2 = {False, "Google", 1, "Amazon", 2, True}
set3 = set1.intersection(set2)
print(set3)