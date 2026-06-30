def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def find_next_leap_year(year):
    """Find the next leap year after the given year."""
    next_year = year + 1
    while not is_leap_year(next_year):
        next_year += 1
    return next_year


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        next_leap = find_next_leap_year(year)
        print(f"The next leap year after {year} is {next_leap}.")
    except ValueError:
        print("Please enter a valid year as an integer.")
