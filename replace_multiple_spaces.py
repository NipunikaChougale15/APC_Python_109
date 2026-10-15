import re

s = "This   sentence    has   extra spaces"
cleaned = re.sub(r'\s+', ' ', s)
print("Cleaned:", cleaned)
