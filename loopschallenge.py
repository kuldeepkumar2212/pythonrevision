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

files = ['report.docx', 'data.csv', 'presentation.pptx', 'report1.docx', 'summary.pdf']

for file in files:
    if files.count(file) > 1:
        print(f"{file} appears more than once in the list.")
        break
else:
    print("All files are unique in the list.")