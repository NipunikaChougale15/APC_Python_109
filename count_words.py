import re

sentence = "Python is very easy to learn"
words = re.findall(r'\b\w+\b', sentence)
print("Word count:", len(words))
