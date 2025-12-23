correct_username = "Harathich"
correct_password = "50daysofpython"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Access Granted")
    else:
        print("Incorrect password")
else:
    print("Username not found.")

