#beginer

#1

# def my_function():
#     city = "kalol"
#     print(city)

# my_function()

#2

# school = "k.v."
# def my_function():
#     print(school)

# my_function()

#3


# if True:
#     city = "surat"

# print(city)

#4

# for i in range(0,5):
#     name = "tarang vaghasiya"

# print(name)

#5

# scope:- where we use variable
# lifetime :- how long variable store in code

#intermediate

#6

# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)

#output
# 200
# 100

#7

# clicks = 0
# def click():
#     global click
#     clicks += 1


#8

# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# #output
# error because variable declare in local but after use in function

#9

# name = "yash"
# def fun1():
#     name = "lavya"
#     def fun2():
#         print(name)
#     fun2()
# fun1()

#10


# def get_fruits():
#     fruits = ["Apple", "Banana", "Mango"]
#     return fruits

# my_list = get_fruits()

# print("Original List:", my_list)

# my_list.append("Orange")

# print("Updated List:", my_list)

#challenging

#11


# def counter():
#     count = 0

#     def increase():
#         nonlocal count
#         count = count + 1
#         return count

#     return increase

# my_counter = counter()

# print(my_counter())
# print(my_counter())
# print(my_counter())

#12

# x = 1
# def outer():
#     x = 2
#     def inner():
#         x = 3
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

#13



#14


# def outer_function():
#     name = "Tarang"

#     def inner_function():
#         print("Hello", name)

#     return inner_function


# my_function = outer_function()

# my_function()

#15


