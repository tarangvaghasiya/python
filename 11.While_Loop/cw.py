
# i=1
# while i <= 3:
#     j =1
#     while j <=3:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# i=1
# while i <= 3:
#     j =1
#     while j <=3:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



# i=1
# while i <= 3:
#     j =1
#     while j <=3:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# i = 5
# while i >= 1:
#     j = i
#     while j >= 1:
#         print("*",end="")
#         j-=1
#     print()
#     i-=1


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1


# i = 1
# while i <= 10:
#     j=1
#     while j <= 10:
#         print(i*j,end="\t")
#         j+=1
#     print()
#     i+=1


# num=5

# while num<=5:
#     j=1
#     while j<=15:
#         print(j,end="")
#         j+=1
#     print()
#     num+=1

# pass1 = int(input("enter 6 digit password:-"))
# time1 = 0
# while pass1 != 420420:
#     print("you enterd pass worng",":-",pass1)
#     if time1 == 5:
#         print("you enterd so time password wrong")
#     else:
#         pass1 = int(input("enter 6 digit password:-"))
#     time1+=1
# print(f"you enterd right password :- {pass1}")
# print("-----loop ended-------")

# number = int(input("Enter a number: "))
# total = 0
# while number != 0:
#     total = total + number
#     number = int(input("Enter a number: "))
# print("Sum:", total)

# str1 =input("enter string :-")
# rstr1 =  str1[::-1]
# if str1 == rstr1:
#     print("sting is pelendrom")
# else:
#     print("string is not pelendrome")

# str1 = input("Enter string: ")
# rstr1 = ""
# i = len(str1) - 1
# while i >= 0:
#     rstr1 += str1[i]
#     i -= 1
# if str1 == rstr1:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# str1 = input("enter string:-")
# i = 0
# j = len(str1) - 1
# flag = True
# while i < j :
#     if str1[i] == str1[j]:
#         i+=1
#         j-=1 
#     else:
#         flag = "false"
#         i=j
# if flag == True:
#     print("string is palandrom")
# else:
#     print("string is not palendrom")


num = int(input("enter your number:-"))
sum = 0
rever=0
while num > 0:
    digit = num % 10
    print(digit,end="")
    num = num // 10
    rever= rever*10 + digit
    sum += digit
print(f"sum of all digit is {sum}")
print(rever)