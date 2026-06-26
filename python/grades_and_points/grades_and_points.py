points = int(input("How many points [0-100]: "))
if points>=0 and points<=49:
    print("fail")
elif points>=50 and points<=59:
    print("1")
elif points>=60 and points<=69:
    print("2")
elif points>=70 and points<=79:
    print("3")
elif points>=80 and points<=89:
    print("4")
elif points>=90 and points<=100:
    print("5")
else:
    print("impossible!")
