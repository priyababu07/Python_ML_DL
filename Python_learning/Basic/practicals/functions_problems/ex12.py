def palindrome(inputval = "malayalam"):
    pal =""
    for i in inputval:
        pal=i+pal
    if pal == inputval:
        print("It is palindrome")
    else:
        print("Not a palindrome")
palindrome("English")
