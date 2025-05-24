def find_number_ofupperlower(inputSt):
    cap=0
    smal=0
    for i in inputSt:
        if i.isupper():
            cap = cap+1
        elif i.islower():
            smal = smal+1
        else:
            continue
    return cap,smal

print(find_number_ofupperlower("My Name is Sugu"))

