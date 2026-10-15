import re

sentence = "This is is a test Test"
repeats = re.findall(r'\b(\w+)\b\s+\b\1\b', sentence, flags=re.IGNORECASE)
print("Repeated words:", repeats)
