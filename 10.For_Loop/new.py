total=0
flag = False
grade = ""


for i in range(5):
    marks = int(input("enterb your marks"))
    if marks <35 :
        flag == False
    total+=marks
   

persetage = total/5

if flag != False:
    if persetage >= 90:
        grade="A+"
    elif persetage >= 80:
        grade="A"
    elif persetage >= 70:
        grade="B"
    elif persetage >= 60:
        grade="C"
    elif persetage >= 50:
        grade="D"
    else:
        grade="f"
else:
    grade="f"

if flag != False:
    print("you are pass")
    print(f"your persetage is :-{persetage}%")
    print(f"your total marks is :-{total}")
    print(f"your grad is :-{grade}")
else:
    print("you are fail")

