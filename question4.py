def get_season(month, day):
    if (month == 3 and day >= 20) or (month == 4 or month == 5) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (month == 7 or month == 8) or (month == 9 and day < 23):
        return "Summer"
    elif (month == 9 and day >= 23) or (month == 10 or month == 11) or (month == 12 and day < 21):
        return "Fall"
    else:
        return "Winter"
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter the year:\n"))
month = int(input("Enter the month:\n"))
day = int(input("Enter the day:\n"))

season = get_season(month, day)
print("Season:", season)

if is_leap_year(year):
    print(f"{year} is a leap year\n")
    days_in_year = 366
else:
    print(f"{year} is not a leap year\n")
    next_leap_year = year + (4 - year % 4)
    print(f"The next leap year after {year} is {next_leap_year}.")
    days_in_year = 365

print(f"Number of days in the year {year}: {days_in_year}")

