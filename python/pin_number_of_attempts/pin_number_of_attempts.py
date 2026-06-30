attempt = 0
while True:
    pin = int(input("PIN: "))
    attempt += 1
    if pin != 4321:
        print("Wrong")
    elif pin == 4321:
        if attempt == 1:
            print("Correct! it only took you one single attempt!")
            break
        elif attempt > 1:
            print(f"Correct! It took you {attempt} attempts")
            break






