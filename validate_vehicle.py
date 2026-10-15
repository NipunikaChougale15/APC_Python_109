import re

vehicle = "MH12AB1234"
if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', vehicle):
    print("Valid vehicle number")
else:
    print("Invalid")
