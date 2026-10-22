# def abb(a,b,/):
#     return a**b + a

# print(abb(2,3))

# def op(a,b,/,oprection = "add"):
#     if oprection == "add":
#         return a+b
#     if oprection == "multi":
#         return a*b

#     return None

# print(op(10,20))
# print(op(10,20,oprection="multi"))

# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Asha")

# def num (*args):
#     print(args)
#     print(type(args))

# num(1,2,3,4,5,6,7)

# def ab (a,v,c):
#     return a+v
# print(ab(2,3,4))

# def add(*args):
#     total = 0

#     for n in args:
#         total += n

#     return total

# print(add(10,20))
# print(add(1,2,3,4,4,5))
# print(add())

# def introduce(name, *hobbies):
#     print("Name:", name)
#     print("Hobbies:", hobbies)

# introduce("Asha", "reading", "cricket", "music")

def ab(a,b,*args):
    print(type(args))
    print(a,b)
    print(args)

ab(1,2,3,4,5,6,7,8,9)