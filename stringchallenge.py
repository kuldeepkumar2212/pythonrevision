#"968-Maria, ( D@t@ Enfineer );; 27y  " clean this string to get the following 
# output: "name: maria | role: Data Engineer | age:27y 

text = "968-,Maria ( D@t@ Enfineer );; 27y  "

name = text.split(",")[1].split("(")[0].strip().lower()
role = text.split('(')[1].split(')')[0].replace('@', 'a').strip()
age = text.split(';;')[1].strip()

print(f"name: {name} | role: {role} | age: {age}")
