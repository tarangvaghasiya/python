# def countdown(n):
#     if n == 0:                 # Base case
#         print("Done!")
#         return

#     print(n)
#     countdown(n - 1)           # Recursive case

# countdown(3)

sum = 0
def sum1(n):
    global sum
    if n == -11:
        return sum
    sum+=n
    return sum1(n-1)
print(sum1(10))
 
def digit_sum(n):
    if n < 10:
        return n

    return n % 10 + digit_sum(n // 10)

snb = digit_sum(472)

def digit_sum(sub):
    if sun < 10:
        return sub

    return sub % 10 + digit_sum(sub // 10)
print(digit_sum(472))