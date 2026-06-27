tax = [100, 1700, 4700, 22100, 142100]
taxr = [0.08, 0.10, 0.12, 0.15, 0.17]
val = [5000, 25000, 55000, 200000, 1000000]

gift = int(input("Value of gift: "))
if gift < 5000:
    print("No tax!")
elif (5000 <= gift <= 25000):
    idx = 0
    ctax = (tax[idx] + (gift - val[idx]) * taxr[idx])
    print(f"Amount of tax: {ctax} euros")
elif (25000 < gift <= 55000):
    idx = 1
    ctax = (tax[idx] + (gift - val[idx]) * taxr[idx])
    print(f"Amount of tax: {ctax} euros")
elif (55000 < gift <= 200000):
    idx = 2
    ctax = (tax[idx] + (gift - val[idx]) * taxr[idx])
    print(f"Amount of tax: {ctax} euros")
elif (200000 < gift <= 1000000):
    idx = 3
    ctax = (tax[idx] + (gift - val[idx]) * taxr[idx])
    print(f"Amount of tax: {ctax} euros")
elif 1000000 < gift:
    idx = 4 
    ctax = (tax[idx] + (gift - val[idx]) * taxr[idx])
    print(f"Amount of tax: {ctax} euros")










