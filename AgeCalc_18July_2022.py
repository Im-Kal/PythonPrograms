# Take both current date and user birthdate and display age.

# Collect user data
print("Now you will be instructed to provide the day, month and year you were born in. Please provide them in number format.")
userage_day = int(input("Please enter the day you were born in using numbers (07, 09, 01 etc) = "))
userage_month = int(input("Please enter the month you were born in using numbers (07, 12, 11 etc) = "))
userage_year = int(input("Please enter the year you were born in using numbers (2007, 2009, 2001 etc) = "))

# Collect info about current date
print("Now you will be instructed to provide the day, month and year today. Please provide them in number format.")
current_day = int(input("Please enter the day today using numbers (07, 09, 01 etc) = "))
current_month = int(input("Please enter the month today using numbers (07, 12, 11 etc) = "))
current_year = int(input("Please enter the year today using numbers (2007, 2009, 2001 etc) = "))


# Main logic
def calc_age():
    result_year = (current_year - userage_year) - 1
    result_month = 12 - (userage_month - current_month)
    result_day = current_day - userage_day

    print("Age in years", result_year)
    print("Age in months", result_month)
    print("Age in days", result_day)


calc_age()
