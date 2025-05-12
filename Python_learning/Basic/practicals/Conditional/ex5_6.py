no_classes = int(input("Enter the number of classes"))
no_class_attended = int(input("Enter the number of classes attended"))
percentage = float(no_class_attended/no_classes)*100
print(percentage,"%")

#modifyed for the 3rd question
 
medical_status= input("Is their any medical condition answer Y/N:")

if medical_status is "Y" and percentage<75:
    print("Eligible for exam")
elif medical_status is "N" and percentage<75:
    print("Not Eligible for Exam")
else:
    print("Eligible for Exam")