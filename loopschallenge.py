#print the n table from 1 to 10 using loops

n = input ("enter the nu,ber for which you want to print the table:")

for i in range(1,11):
    print(f"{n} * {i} = {int(n)*i}")