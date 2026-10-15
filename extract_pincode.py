import re

text = "My PIN is 416012 and office PIN is 400001"
pins = re.findall(r'\b\d{6}\b', text)
print("PIN codes:", pins)
