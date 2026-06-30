year = int(input("Year: "))

next_year = year + 1

while True:
    # Check if next_year is a leap year
    is_leap = (next_year % 400 == 0) or (next_year % 4 == 0 and next_year % 100 != 0)
    
    if is_leap:
        print(f"The next leap year after {year} is {next_year}")
        break
    
    next_year += 1
