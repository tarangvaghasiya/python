#1
 
name=input("Enter your name: ")
print("Hello", name)

#2
city=input("Enter your city: ")
print(f"you are from {city}")

#3
name1=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"Hello {name1}, you are {age} years old")

#4
print("return in str")

#5
a=input("Enter a number: ")
print(type(a))

#6
fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
print(f"Hello {fname} {lname}")

#7
name2=input("Enter your name: ")
age1=int(input("Enter your age: ")) 
city1=input("Enter your city: ")
college=input("Enter your college name: ")

#8
fname1,lname1=map(str, input("Enter your first name and last name: ").split())
print(f"Hello {fname1} {lname1}")

#9
b,c=map(str, input("Enter python programming:").split())
print(f"Python programming: {b} and {c}")

#10
d,e,f=map(str, input("Enter your name, age and city: ").split())
print(f"Hello {d}")
print(f"You are {e} years old")
print(f"You are from {f}")

#11
g=input("Enter your number:")
g=int(g)

#12
h=input("Enter your number:")
h=float(h)

#13
i=input("Enter your number:")
i=int(i)

#14
j=int(input("Enter your number:"))
print(type(j))

#15
k=float(input("Enter your number:"))
print(type(k))

#17

l,m=map(int, input("Enter your first number and last number: ").split())
print(l+m)

#18

name3="rahul"
age2=20
print(f"my name is {name3} and my age is {age2}")

#19

n=10
o=20
print(f"sum of {n} and {o} is {n+o}")

#20

name4=input("Enter your name: ")
age3=int(input("Enter your age: "))
print(f"Hello {name4}, you are {age3} years old")

#21

price,product=map(str, input("Enter the price and product name: ").split())
print(f"Price of {product} is {price}")
price=int(price)
print(product*price)

#22
print("use of :.2f for 2 decimal points in float and round off the value")

#23
product_name=input("Enter your product name: ")
product_price=float(input("Enter your product price: "))
quantity=int(input("Enter your product quantity: "))
print(f"Product name: {product_name} and product price: {product_price:.2f} and product quantity: {quantity}")

#24
print("A", "B", "C")

#25
print("2026", "08", "19")

#26
print("Hello", end=" ")
print("World")

#27
p=int(input("Enter your first number: "))
q=int(input("Enter your second number: "))
print(f"sum of {p} and {q} is {p+q}")

#28
price1=float(input("Enter your product price: "))
quantity1=int(input("Enter your product quantity: "))
print(f"Total cost: {price1 * quantity1:.2f}")

#29
name5=input("Enter your name: ")
age4=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))
print(f"Hello {name5}, you are {age4} years old and your marks are {marks:.2f}")

#30
student_name=input("Enter your name: ")
student_age=int(input("Enter your age: "))
student_city=input("Enter your city: ")
student_height=float(input("Enter your height in meters: "))
print(f"Hello {student_name}, you are {student_age} years old, from {student_city}, and your height is {student_height:.2f} meters.")
print(f"student's heaight in centimeters: {student_height:.2f}")