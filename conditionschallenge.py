#validate the quality and correctness of the email address
# 1.must not be empty
# 2.must contain @ and .
# 3.must contin only one @
# 4.must end with .com, .org, .edu, .net    
# 5. charater limits must be 254 characters
# 6. must start and end with a letter or digit

email = input("Enter your email address: ")
if email == '':
    print("Email address must not be empty.")
else:
    if email.count('@') != 1:
        print("Email address must contain exactly one '@' symbol")
    elif not (email.endswith('.com') or email.endswith('.org') or email.endswith('.edu') or email.endswith('.net')):
            print("Email address must end with .com, .org, .edu, or .net")
    else:
        if len(email) > 254:
            print("Email address must not exceed 254 characters.")
        elif not (email[0].isalnum() and email[-1].isalnum()):               
            print("Email address must start and end with a letter or digit.")
        else:
                print("Email address is valid.")    