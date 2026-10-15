import re

code = "ABC-1234-XY"
if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid product code")
else:
    print("Invalid")
