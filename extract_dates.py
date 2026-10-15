import re

text = "My DOB is 15-10-2000 and exam on 01-12-2026"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)
