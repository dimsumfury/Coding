ltr1 = input("1st letter: ")
ltr2 = input("2nd letter: ")
ltr3 = input("3rd letter: ")

if (ltr2 <= ltr1 <= ltr3) or (ltr3 <= ltr1 <= ltr2):
    print(f"The letter in the middle is {ltr1}")
elif (ltr1 <= ltr2 <= ltr3) or (ltr3 <= ltr2 <= ltr1):
    print(f"The letter in the middle is {ltr2}")
else:
    print(f"The letter in the middle is {ltr3}")


