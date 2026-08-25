#print the n table from 1 to 10 using loops

#n = input ("enter the nu,ber for which you want to print the table:")

#for i in range(1,11):
#    print(f"{n} * {i} = {int(n)*i}")
     
#print the left aligned pyramid of stars using loops as below if n = 3
# *
# **
# ***

#n = int(input ("enter the nuber of rows:"))
#for i in range(n):
#    for j in range(i+1):
#        print("*", end="")
#    print()

#check if the file name appers more than once in the list of files using loops

#files = ['report.docx', 'data.csv', 'presentation.pptx', 'report1.docx', 'summary.pdf']

#for file in files:
#    if files.count(file) > 1:
#        print(f"{file} appears more than once in the list.")
#        break
#else:
#    print("All files are unique in the list.")

#to get an yes input for the user using loops
#1. allow only 3 attempts to get a valid input
#2. if the user fails to provide a valid input after 3 attempts, print "You have exceeded the maximum number of attempts."
#3. if the user provides a valid input, print "Thank you for your response."

n = 3

while n > 0: 
    response = input("Please enter 'yes' or 'no': ").lower()
    if response == 'yes':
        print("Thank you for your response.")
        break
    else:
        n -= 1
        if n == 0:
            print("You have exceeded the maximum number of attempts.")
        else:
            print(f"Invalid input enter yes. You have {n} attempts left.") 
            