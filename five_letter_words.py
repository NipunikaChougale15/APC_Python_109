import re

sentence = "There are apple mango peach grapes"
words = re.findall(r'\b\w{5}\b', sentence)
print("Five-letter words:", words)
