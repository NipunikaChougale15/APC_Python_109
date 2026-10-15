import re

email = "test@example.com"
if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
    print("Valid email")
else:
    print("Invalid")
