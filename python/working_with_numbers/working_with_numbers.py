rpt = 0
neg = 0
pos = 0
sum = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    rpt += 1
    sum += num
    if num < 0:
        neg += 1
    if num > 0:
        pos += 1
   
print("Numbers typed in ", rpt)
print("The sum of the numbers is ", sum)
print(f"The mean of the numbers is {sum/rpt}")
print(f"Positive numbers {pos}")   
print(f"Negative numbers {neg}") 
