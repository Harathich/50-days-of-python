birth_year = int(input("Enter your Birth Year: "))
current_year = int(input("Enter current year: "))
current_month = int(input("Enter current month: "))
if birth_year > 2025:
    print("You haven't been born yet, time traveler!")
else:
    if birth_year < 1900:
        print("You are extraordinality old")

    birth_month = int(input("Enter birth month(1-12): "))
    Age = current_year - birth_year
    if birth_month>current_month:
        Age = Age -1
    print(Age)
