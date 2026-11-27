# 1

# def even_position_sum(n):
#     if n == 0:
#         return 0

#     return (n // 10) % 10 + even_position_sum(n // 100)


# print(even_position_sum(583246)) 

# 2

# def revers(n , r = 0):
#     if n == 0:
#         return r

#     return revers(n//10 , r*10 + n%10)


# print(revers(583246)) 

# 3

# def palndrom(text):
#     if len(text) <= 1:
#         return True

#     if text[0] != text[-1]:
#         return False

#     return palndrom(text[1:len(text)-1])


# print(palndrom("level")) 
# print(palndrom("madam"))  

# 4

# def count(text,ch):
#     if len(text) == 0:
#         return 0
#     if text[0] == ch:
#         return 1+ count(text[1:],ch)
#     else :
#         return count(text[1:],ch)
# print(count("programming","m"))

# 5

# def commun(a, b):
#     if b == 0:
#         return a

#     return commun(b, a % b)


# print(commun(18, 48)) 

# 6

# def is_prime(n, i=2):
#     if n == i:
#         return True

#     if n % i == 0:
#         return False

#     return is_prime(n, i + 1)


# print(is_prime(29))  
# print(is_prime(10)) 

# 7

# 8

# ans = ""
# def binery(n):
#     global ans
#     if n <= 0:
#         return
#     rem = n % 2
#     binery(n//2)
#     ans += str(rem)
    
# binery(13)
# print(ans)

# 9

# 10

# def digital_root(n):
#     if n < 10:
#         return n

#     total = 0

#     while n > 0:
#         total = total + n % 10
#         n = n // 10

#     return digital_root(total)


# print(digital_root(9875))