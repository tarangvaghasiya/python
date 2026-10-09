# choice = 3

# match choice:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Other")

# day = int(input("enter day number:-"))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid")


# a = int(input("enter number:-"))
# b = int(input("enter number:-"))
# c=0
# while True:
#     print("1->+\n2->-\n3->*\n4->/\n5->%\n6->**\n7->//\n0->leave")
#     op = int(input("enter oprection number"))
#     if op == 0:
#         break
#     match op:
#         case 1:
#             c=a+b
#         case 2:
#             c=a-b
#         case 3:
#             c=a*b
#         case 4:
#             c=a/b
#         case 5:
#             c=a%5
#         case 6:
#             c=a**b
#         case 7:
#             c=a//b
#         case _:
#             print("enter valid opretion")
#             continue

#     print(f"oprection {c}")


# num = int(input("enter number:-"))
# i=1
# c1=0
# while i <=num:
#     if num %i == 0:
#         c1+=1
#     i+=1
# if c1 > 2:
#     print("not a prime number")
# else:
#     print("prime number")

# marks = int(input("enter marks:-"))

# match marks:
#     case y if y >= 90:
#         print("A")
#     case y if y >= 75:
#         print("B")
#     case y if y >= 60:
#         print("C")
#     case y if y >= 40:
#         print("D")
#     case _:
#         print("Fail")

# account = "student"
# choice = int(input("enter choise:-"))
# match account:
#     case "student":
#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")
#     case "teacher":
#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")
#     case _:
#         print("Invalid Account Type")

cc = "caller"
choise = int(input("enter choise:-"))

match cc:
    case "caller":
        match choise:
            case 1:
                print("normal employ")
            case 2:
                print("high level worker")
            case 3:
                print("manger")
            case 4:
                print("deparment head")
            case _:
                print("enter vadild number")
    case "worker":
        match choise:
            case 1:
                print("ask for salary")
            case 2:
                print("for any qrary")
            case 3:
                print("manger")
            case 4:
                print("diector")
            case _:
                print("enter vadild number")
    case _:
        print("enyet valid role")

