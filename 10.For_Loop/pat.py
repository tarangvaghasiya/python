# print("*   *")
# print("*   *")
# print("*   *")
# print("*   *")
# print("*****")


# n = int(input("enterb your rows:-"))
# for i in range(n):
#     if i == (n-1):
#         print("* * * * *")
#     else:
#         print("*       *")

n=int(input("Enter any integer:-"))  
for i in range(1,n+1):
    for j in range(1,n+1):
      if j==1 or j==n or i==n or (j==((n+1)/2) and i==((n+1)/2)) or (j==((n+1)//2) and i==((n+1)//2)):
         print("*", end=" ")
      else:
         print(" ", end=" ")
    print()
