import re

code = "x = 10  # this is a comment"
comments = re.findall(r'#.*', code)
print("Comments:", comments)
