Str=input("enter yiur string:-").strip()
Str2=""
length=len(Str)
for element in range(length-1,-1,-1):
  Str2=Str2+Str[element]
print(f"revert str is :-{Str2}")
if Str == Str2:
    print("string is reversable")
else:
    print("string is not reversable")
name = "Rahul"