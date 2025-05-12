#Enter the marks and get the grade
mark = int(input("Enter the mark:"))
if mark<25:
    print("Grade F")
elif 25<=mark<45:
    print("Grade E")
elif 45<=mark<50:
    print("Grade D")
elif 50<=mark<60:
    print("Grade C")
elif 60<=mark<80:
    print("Grade B")
elif mark>=80:
    print("Grade A")
else:
    print("Invalid")