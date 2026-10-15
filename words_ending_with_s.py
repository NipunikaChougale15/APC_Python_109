import re

sentence = "Cats dogs birds fish"
words = re.findall(r'\b\w+s\b', sentence)
print("Words ending with s:", words)
