import re

text = "Name: Rahul Roll: 101 Marks: 85"
names = re.findall(r'Name:\s*(\w+)', text)
rolls = re.findall(r'Roll:\s*(\d+)', text)
marks = re.findall(r'Marks:\s*(\d+)', text)
print("Names:", names, "Rolls:", rolls, "Marks:", marks)
