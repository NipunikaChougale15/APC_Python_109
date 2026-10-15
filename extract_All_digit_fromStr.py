import re

s = "My phone number is 9876543210"
digits = re.findall(r'\d', s)
print("Digits:", digits)
