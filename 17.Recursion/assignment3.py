# 1

# def msg(m, n):
#     if n == 0:
#         return

#     print(m)
#     msg(m, n - 1)


# msg("Hello", 3)


# 2

# def even(n):
#     if n < 2:
#         return

#     even(n - 2)
#     print(n, end=" ")


# even(10)


# 3

# def odd(n):
#     if n <= 0:
#         return 0

#     if n % 2 == 0:
#         return odd(n - 1)

#     return n + odd(n - 2)


# print(odd(7))


# 4

# def cnt(n, d):
#     if n == 0:
#         return 0

#     if n % 10 == d:
#         return 1 + cnt(n // 10, d)

#     return cnt(n // 10, d)


# print(cnt(52525, 5))


# 5

# def prod(n):
#     if n < 10:
#         return n

#     return (n % 10) * prod(n // 10)


# print(prod(234))


# 6

# def first(n):
#     if n < 10:
#         return n

#     return first(n // 10)


# print(first(5837))


# 7

# def find(n, d):
#     if n == 0:
#         return d == 0

#     if n % 10 == d:
#         return True

#     return find(n // 10, d)


# print(find(4826, 8))


# 8

# def count(s):
#     if s == "":
#         return 0

#     return 1 + count(s[1:])


# print(count("coding"))


# 9

# def vowel(s):
#     if s == "":
#         return 0

#     if s[0] in "aeiou":
#         return 1 + vowel(s[1:])

#     return vowel(s[1:])


# print(vowel("education"))


# 10

# def pal(s):

#     def check(l, r):
#         if l >= r:
#             return True

#         if s[l] != s[r]:
#             return False

#         return check(l + 1, r - 1)

#     return check(0, len(s) - 1)


# print(pal("level"))
