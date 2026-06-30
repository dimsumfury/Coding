pwd = input("Password: ")
while True:
    rpwd = input("Repeat password: ")
    if pwd != rpwd:
        print("They do not match!")
    elif pwd == rpwd:
        print("User account created!")
        break
