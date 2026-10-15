import re

number = "9876543210"
if re.fullmatch(r'[6-9]\d{9}', number):
    print("Valid mobile number")
else:
    print("Invalid")
