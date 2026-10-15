import re

sentence = "Apples and Mangoes are awesome and Amazing"
words = re.findall(r'\b[Aa]\w*', sentence)
print("Words starting with A/a:", words)
