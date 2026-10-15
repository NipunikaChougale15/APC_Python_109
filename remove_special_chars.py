import re

s = "Hello@World! 123 #Python"
cleaned = re.sub(r'[^A-Za-z0-9 ]', '', s)
print("Cleaned:", cleaned)
