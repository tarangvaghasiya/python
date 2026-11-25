#1
# Base case — tells the function when to stop.
# Recursive case — calls the function again with a smaller or simpler problem.

#2

# if a base case is missing or unreachable in recursion, the function may call itself repeatedly without stopping.

#3

# the main difference is return sends the calculated value back to the calling function, while n + sum_to(n - 1) only calculates the value and does not return it.


#4

# code after a recursive call runs AFTER the deeper recursive call finishes.

#5

# the simple recursive Fibonacci function is slow for large inputs because it calculates the same Fibonacci values multiple times.

##########################################################################################################################################

#1

# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)

# show(2)

#output
# 2
# 1
# Stop
# 1
# 2

#2

# def total(n):
#     if n == 0:  #base case
#         return 0

#     return n + total(n - 1)

#3

# def count(n):
#     if n == 0:
#         return

#     count(n + 1)


#infinity

#4

# def answer(n):
#     if n == 0:
#         return 0

#     return n + answer(n - 1)

# print(answer(3))

# 6

########################################################################################################

#5

# def countdown(n):
#     if n == 0:
#         print("done!")
#         return
#     print(n)
#     countdown(n - 1)
# countdown(3)

#6
# a = 1
# def count_up(n):
#     global a
#     if a == n:
#         print(n)
#         return
#     print(a)
#     a +=1
#     count_up(n)
# count_up(5)

#7

# sum = 0
# a = 0
# def sum1(n):
#     global sum , a

#     if a == n+1:
#         print(sum)
#         return
#     sum += a
#     a +=1
#     sum1(n)
# sum1(5)

# 8

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)


# print(factorial(4))  
# print(factorial(0))  

#9

# def digit_sum(n):
#     if n == 0:
#         return 0

#     return (n % 10) + digit_sum(n // 10)


# print(digit_sum(583))  
# print(digit_sum(7))    
# print(digit_sum(0))    

#10

# def power(x, y):
#     if y == 0:
#         return 1

#     return x * power(x, y - 1)


# print(power(2, 5))
# print(power(9, 0))
# print(power(3, 1))

#11

# def count_digits(n):
#     if n < 10:
#         return 1

#     return 1 + count_digits(n // 10)


# print(count_digits(5382)) 
# print(count_digits(6))     
# print(count_digits(0))     

#12

# def reverse_text(text):
#     if text == "":
#         return ""

#     return reverse_text(text[1:]) + text[0]


# print(reverse_text("cat"))
# print(reverse_text("a"))  
# print(reverse_text(""))

#13

# def Fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return Fibonacci(n -1) + Fibonacci(n - 2)
# print(Fibonacci(0))
# print(Fibonacci(1))
# print(Fibonacci(6))

#14

# def max_digit(n):

#     if n < 10:
#         return n

#     last_digit = n % 10

#     remaining_max = max_digit(n // 10)

#     if last_digit > remaining_max:
#         return last_digit
#     else:
#         return remaining_max

# print(max_digit(4987))

#15

# def mystery(n):
#     if n <= 1:
#         return n

#     return mystery(n - 1) + mystery(n - 2)

# mystery(0)   0
# mystery(1)   1
# mystery(2)   1

#16

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

#17

# def stop_at_zero(n):
#     if n == 0:
#         return

#     stop_at_zero(n - 1)