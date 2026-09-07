# a=(int(input("Enter a number: ")))

# if a % 2 == 0:

#     print("your number is Even")
# else:

#     print("your number is Odd")


# age=int(input("Enter your age: ").split()[0])

# if age >= 18:

#     print("You are eligible to watch this movie")

#     gender=str(input("Enter your gender: ").split()[0])

#     if gender == "male":

#         print("Your ticket price is 300-500")

#         class_input=int(input("Enter your class(1,2,3): "))

#         if class_input == 1:

#             print("Your ticket price is 500")

#         elif class_input == 2:

#             print("Your ticket price is 400")

#         elif class_input == 3:

#             print("Your ticket price is 300")    

#     elif gender == "female":

#         print("Your ticket price is 100-300")

#         if class_input == 1:

#             print("Your ticket price is 300")

#         elif class_input == 2:

#             print("Your ticket price is 200")

#         elif class_input == 3:

#             print("Your ticket price is 100") 
# else:

#     print("You are not eligible to watch this movie")

a=int(input("enter your first number"))

b=int(input("enter your second number"))

# a,b=map(int(input("input your num").split()))


print("1.addition\n2.subtaration\n3.multiplication\n4.division\n5.flor division\n choose your opretion")


# a1= a+b

# a2= a-b

# a3= a*b

# a4= a/b

# a5= a//b


aop=int(input("eneter your opretion number"))

if aop == 1:

    print(a+b)

elif aop == 2:

    print(a-b)

elif aop == 3:

    print(a*b)

elif aop == 4:

    print(a/b)

elif aop == 5:

    print(a//b)
else:
    print("you choose other number")


