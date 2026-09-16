# a=int(input("eneter rows:-"))
# b=int(input("enter columns:-"))
# for rows in range(a):
#     for columns in range(b):
#         print("*",end="")
#     print()

# for i in range(0,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# for i in range(0,6):
#     for j in range(1,6-i):
#         print(j,end="")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n = int(input("enter your number"))
# for i in range(1, n+1):
#     for j in range(1,(n+1) - i):
#         print(" ", end="")
#     for k in range(1,i+1):
#         print(k, end="")
#     print()

for i in range(1,6):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range(1,6-i):
        print("*",end="")    
    print()