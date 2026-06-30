year = int(input("Please type in a year: "))
leap_year = False
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True

if leap_year:
    print(f"The next leap year after {year} is {year + 4}")

while False:
    year += 1
    if leap_year:
        year + 4
        print(f"The next leap year after {year} is {year + 4}")
        break


