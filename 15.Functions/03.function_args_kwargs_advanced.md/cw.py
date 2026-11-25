# def abb(a,b,/):
#     return a**b + a

# print(abb(2,3))

# def op(a,b,/,oprection = "add"):
#     if oprection == "add":
#         return a+b
#     if oprection == "multi":
#         return a*b

#     return None

# print(op(10,20))
# print(op(10,20,oprection="multi"))

# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Asha")

# def num (*args):
#     print(args)
#     print(type(args))

# num(1,2,3,4,5,6,7)

# def ab (a,v,c):
#     return a+v
# print(ab(2,3,4))

# def add(*args):
#     total = 0

#     for n in args:
#         total += n

#     return total

# print(add(10,20))
# print(add(1,2,3,4,4,5))
# print(add())

# def introduce(name, *hobbies):
#     print("Name:", name)
#     print("Hobbies:", hobbies)

# introduce("Asha", "reading", "cricket", "music")

# def ab(a,b,*args):
#     print(type(args))
#     print(a,b)
#     print(args)

# ab(1,2,3,4,5,6,7,8,9)

# def abb(c,d=20,*args):
#     print(type(args))
#     return args , c+d
# print(abb(14,15,2,32,57,69))

# def abb(c,*args,d = 20,**kwargs):
#     print(type(kwargs))
#     print(type(args))
#     return args , kwargs , c+d
# print(abb(10,20,30,40,50,60,Tarang="420",d=12))

# def abb(a,b,*print1):
#     for i in print1:
#         print(i)
#     return a , b , print1

# print(abb(1,2,3,4,5,6,7,8,9))

# def print_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# print_profile(name="Tarang", age=18, course="AI",birthdate = "07-05-2009", add = "surat")
 
# asd = (1,)
# print(type(asd))




# s = input("Enter main string: ")
# sub = input("Enter substring: ")
# i = 0
# while i < len(s):
#     j = 0
#     while j < len(sub):
#         if s[i + j] != sub[j]:
#             break
#         j += 1
#     if j == len(sub):
#         print("Found at index:", i)
#         break
#     i += 1
# else:
#     print("Not found")


# s = input("Enter a string: ")
# i = 0
# while i < len(s):
#     count = 0
#     j = 0
#     while j < len(s):
#         if s[i] == s[j]:
#             count = count + 1
#         j = j + 1
#     print(s[i], ":", count)
#     i = i + 1

# def add(a,b,c):
#     return a+b+c
# print(add(a=10,b=20,c=30))

# s = input("Enter a string: ")
# i = 0
# while i < len(s):
#     count = 1
#     while i + 1 < len(s) and s[i] == s[i + 1]:
#         count = count + 1
#         i = i + 1
#     print(s[i] + str(count), end="")
#     i = i + 1

# s = input("Enter a string: ")

# i = 0

# while i < len(s):
#     count = 0
#     j = 0
#     found = 0

    # while j < i:
    #     if s[i] == s[j]:
    #         found = 1
    #     j = j + 1

    # if found == 0:
    #     j = 0

    #     while j < len(s):
    #         if s[i] == s[j]:
    #             count = count + 1
    #         j = j + 1

    #     print(s[i] + str(count), end="")

    # i = i + 1


# s = input("enter a string:-")
# i =0
# while i < len(s):
#     f = int(s[i+1])
#     print(s[i]*f,end="")
#     i +=2

# s = input("enter a string:-")
# sub = input("enter what you want do found in string:-")
# i = 0
# while i < len(s):
#     j =0 
#     while j < len(sub):
#         if s[i] == sub[j]:
#             i+=1
#             j+=1
#         else:
#             break
        

#     if j == len(sub):
#         print("found")
#         break
#     i+=1
# else:
#     print("not found")

# str = input("Enter your string:-").lower()
# Length=len(str)
# mid = (Length//2)
# str1 = str[0:mid] 
# str2 = str[mid:] 
# if str1 == str1[::-1] and str2 == str2[::-1]:
#     print("Palindrome")
# else:
#     print("Divided parts are not palindrome")

# s = input("Enter string: ")

# result = ""
# i = 0

# while i < len(s):
#     char = s[i]
#     i = i + 1

#     num = ""

#     while i < len(s) and s[i].isdigit():
#         num = num + s[i]
#         i = i + 1
#     result = result + char * int(num)
# print(result)

