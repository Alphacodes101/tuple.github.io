# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry","apple","cherry")
print(mytuple)


# Tuple items are ordered, unchangeable, and allow duplicate values.

# tuple length 
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# create tuple with one item 
thistuple1= ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))

#tuple itmes in data types 
tuple3=("apple","bannana","cherry")
tuple4=(1,5,7,9,3)
tuple5=(True,False,False)

print(tuple3)
print(tuple4)
print(tuple5)
print(type(tuple3))
print(type(tuple4))
print(type(tuple5))

# access the tuple data 
thistuple6=("apple","bannana","cheery")
print(thistuple6[0])

# negative indexing
thistuple7=("apple","bannana","cherry")
print(thistuple7[-1])

# range of indexing 
thistuple8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple8[2:5])

# check items exits
thistuple9=("apple","bannana","cherry")
if "apple" in thistuple9:
    print("yes,'apple' is in the fruits tuple")
    
    
# change tuple value
""" Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add items
# 1.Convert into a list 
thistuple10 = ("apple", "banana", "cherry")
y = list(thistuple10)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple
thistuple11 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple11 += y

# print(thistuple11)


# upacking a tuple, means  tuples is outside barcket....
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)
