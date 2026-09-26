#1

num1 = int(input("enter your number:-"))
num2 = int(input("enter your number:-"))
print(f"sum of your number:-{num1+num2}")

#2

num3 = int(input("enter your number:-"))
if num3%2 == 0:
    print("your number is even")
elif num3%2 != 0:
    print("your number is odd")
else:
    print("enter valid value")


#4

age = int(input("enter your age:-"))
if age > 18:
    print("you are eligible")
else:
    print("you are not eligible")