# a=int(input("eneter rows:-"))
# b=int(input("enter columns:-"))
# for rows in range(a):
#     for columns in range(b):
#         print("*",end="")
#     print()

for i in range(0,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(0,6):
    for j in range(1,6-i):
        print(j,end="")
    print()
