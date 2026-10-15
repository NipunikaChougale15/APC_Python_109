import re

html = "<p>Hello,   world!!!</p>"
cleaned = re.sub(r'<.*?>', '', html)       # remove tags
cleaned = re.sub(r'\s+', ' ', cleaned)     # normalize spaces
cleaned = re.sub(r'[^\w\s]', '', cleaned)  # remove punctuation
print("Cleaned:", cleaned)
