#validate the quality and correctness of password
# 1.must not be empty
# 2. must be atleast 8 characters long
# 3. must contain atleast one uppercase letter
# 4. must contain atleast one lowercase letter
# 5. must not be the same as the email address
# 6.must not contain and spaces
# 7. must start with a letter  or a digit

email = "kuldeepkumar@gmail.com"
password = input("Enter your password: ")

if password == '':
    print("password must not be empty.")
else:
    if len(password) < 8:
        print("password must be atleast 8 characters long.")
    elif password == email:
        print("password must not be the same as the email address.")
    elif ' ' in password:
        print("password must not contain any spaces.")
    elif not (password[0].isalnum()):
        print("password must start with a letter or a digit.")
    elif not any(char.isupper() for char in password):
        print("password must contain atleast one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("password must contain atleast one lowercase letter.")
    else:
        print("password is valid.")
        