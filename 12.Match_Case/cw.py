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


a = int(input("enter number:-"))
b = int(input("enter number:-"))
c=0
while True:
    print("1->+\n2->-\n3->*\n4->/\n5->%\n6->**\n7->//\n0->leave")
    op = int(input("enter oprection number"))
    if op == 0:
        break
    match op:
        case 1:
            c=a+b
        case 2:
            c=a-b
        case 3:
            c=a*b
        case 4:
            c=a/b
        case 5:
            c=a%5
        case 6:
            c=a**b
        case 7:
            c=a//b
        case _:
            print("enter valid opretion")
            continue

    print(f"oprection {c}")

