import re

text = "Line1\tLine2\nLine3 Line4"
matches = re.findall(r'[ \t\n]', text)
print("Spaces/Tabs/Newlines:", matches)
