import re

s = "Regular Expressions are powerful"
vowels = re.findall(r'[aeiouAEIOU]', s)
print("Vowel count:", len(vowels))
