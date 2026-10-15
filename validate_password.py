import re

password = "Abc@1234"
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid")
