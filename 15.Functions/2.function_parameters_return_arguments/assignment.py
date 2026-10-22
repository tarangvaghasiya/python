#1

# def Welcome():
#     print("welcome to python")
# Welcome()
# Welcome()
# Welcome()

#2

# def greet(name):
#     print(f"welcome {name}")
# greet("tarang")

#3

# def number(num):
#     return num

# print(number(99))

#4

# def sum(a,b):
#     return a+b
# print(sum(10,20))

#5

# def squr(num):
#     return num**2

# print(squr(3))

#6

# def even(num):
#     if num%2 == 0:
#         even = True
#     else:
#         even = False
#     return even

# print(even(99))

#7

# def fulln(fname , lname):
#     return fname + lname
# print(fulln("tarang","vaghasiya"))

#8

# def info(name , city = "surat"):
#     return f"i am {name} from {city}"
# print(info("tarang"))

#9

# def subtract(a, b):
#     print(a - b)

# subtract(10, 3)
# subtract(3, 10)

#10

# def get_min_max(a, b):
#     if a < b:
#         return a, b
#     else:
#         return b, a

# small, large = get_min_max(10, 5)

# print("Smaller:", small)
# print("Larger:", large)

#11

# def calculate(a, b):
#     return a + b, a - b, a * b, a / b

# sum_result, difference, product, quotient = calculate(10, 2)

# print("Sum:", sum_result)
# print("Difference:", difference)
# print("Product:", product)
# print("Quotient:", quotient)

#12

# def count_digits(number):
#     if number == 0:
#         return 1

#     count = 0

#     while number > 0:
#         count = count + 1
#         number = number // 10

#     return count

# print(count_digits(123450))
# print(count_digits(0))

#13

# def classify_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"


# print(classify_number(10))
# print(classify_number(-5))
# print(classify_number(0))

#14

# def calculate_total(price, quantity=1):
#     return price * quantity

# print(calculate_total(100))
# print(calculate_total(100, 3))

#15

# def create_email(username, domain="example.com"):
#     return username + "@" + domain

# print(create_email("tarang"))
# print(create_email("rahul", "gmail.com"))

#16

# def format_name(first, last, uppercase=False):
#     full_name = first + " " + last

#     if uppercase == True:
#         return full_name.upper()
#     else:
#         return full_name

# print(format_name("Tarang", "Vaghasiya"))
# print(format_name("Tarang", "Vaghasiya", True))

#17

# def percentage(marks, total=100):
#     return (marks / total) * 100

# print(percentage(80))
# print(percentage(450, 500))

#18

# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute

# print(convert_minutes(5))
# print(convert_minutes(2, 60))

#19

# def student_details(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)

# student_details(city="Surat", name="Tarang", age=18)

#20

# def bill(item, quantity=1, price=100):
#     return quantity * price

# print(bill("Pen"))
# print(bill("Book", 2, 50))
# print(bill(item="Pencil", price=10, quantity=5))

#21

# def analyze_number(number):
#     if number < 0:
#         absolute_value = number * -1
#     else:
#         absolute_value = number
#     if number % 2 == 0:
#         is_even = True
#     else:
#         is_even = False
#     digits = len(str(absolute_value))
#     return absolute_value, is_even, digits
# print(analyze_number(-246))

#22

# def calculate_stats(a, b, c):
#     smallest = a
#     largest = a

#     if b < smallest:
#         smallest = b
#     if c < smallest:
#         smallest = c

#     if b > largest:
#         largest = b
#     if c > largest:
#         largest = c

#     total = a + b + c

#     return smallest, largest, total


# print(calculate_stats(10, 5, 20))


#23

# def make_sentence(subject, verb, object):
#     return subject + " " + verb + " " + object


# sentence = make_sentence(
#     object="Python",
#     subject="I",
#     verb="love"
# )

# print(sentence)

#24

# def apply_discount(price, discount=0):
#     discount_amount = price * discount / 100
#     final_price = price - discount_amount
#     return final_price
# print(apply_discount(1000, 20))
# print(apply_discount(500))

#25

# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus


# print(calculate_pay(5))
# print(calculate_pay(5, 300))
# print(calculate_pay(5, bonus=100))
# print(calculate_pay(5, rate=300, bonus=100))
# print(calculate_pay(bonus=50, hours=4, rate=250))

#26

# def get_coordinates(x=0, y=0):
#     return x, y


# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))

#27

# def compare(a, b):
#     if a > b:
#         message = "A is greater"
#         difference = a - b
#     elif b > a:
#         message = "B is greater"
#         difference = b - a
#     else:
#         message = "Equal"
#         difference = 0

#     return message, difference


# print(compare(10, 5))
# print(compare(3, 8))
# print(compare(7, 7))

#28

# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     else:
#         return (value - 32) * 5 / 9


# print(convert_temperature(25))
# print(convert_temperature(100, "C"))
# print(convert_temperature(98.6, "F"))

#29

# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"

# print(calculate_result(40))
# print(calculate_result(30))
# print(calculate_result(60, 50))

#30

def order_summary(item, quantity=1, price=100, delivery_fee=40):
    total = quantity * price + delivery_fee
    return total
print(order_summary("Book", delivery_fee=60))