import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
total_pool = letters + numbers + symbols

pwd_len = int(input("How long do you want the password? "))
password = ""
if pwd_len<8:
    print("That is too short, generating a strong password.")
    for i in range(0,8):
        password = password + random.choice(total_pool)
else:
    for i in range(pwd_len):
        password = password + random.choice(total_pool)

print(f"Your password is: {password}")