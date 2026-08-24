#generate a random integer between 1 and 100 and check if the result is even

import random

x=random.randint(1,100) 
print(x)

if x % 2 == 0:
    print("The generated random integer is even.")
else:
    print("The generated random integer is odd.")