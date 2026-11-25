# total = 100
# def greet():
#     global total
#     total += 10
#     print(total)

# greet()
# print(total)

# def fun(a,b=[]):
#     b.append(a)
#     return b

# print(fun(9))
# print(fun(9))
# print(fun(9))
# print(fun(9,[]))
# print(fun(9),fun(9),fun(9))

# def fun (a,b=[]):
#     b.append(a)
#     print(b)
# fun(9) b 
# fun(9)
# fun(9)

# message = "global"

# def outer():
#     message = "enclosing"

#     def inner():
#         global message
#         message = message + "added"
#         print(message)

#     inner()

# outer()

# print(message)


# def make_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# counter = make_counter()
# print(counter())
# print(counter())
# print(counter())


# def sum_to(n):
#     if n == 0:
#         return 0

#     return n + sum_to(n - 1)

# print(sum_to(int(input("enter a number:- "))))

# def digit_sum(n):
#     if n < 10:
#         return n

#     return n % 10 + digit_sum(n // 10)

# print(digit_sum(int(input("Enter a number: "))))