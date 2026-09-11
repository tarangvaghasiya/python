has_id=input("you have id(yes/no): ").strip().lower()
if has_id=="no":
    has_id=False
    print("go to home")
elif has_id=="yes":
    has_id=True
    print("aavi jao")
else:
    print("enter valid valuye")