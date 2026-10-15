import re

s = "Hello World PYthon"
caps = re.findall(r'[A-Z]', s)
print("Uppercase letters:", caps)
