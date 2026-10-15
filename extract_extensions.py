import re

files = "report.pdf image.jpeg notes.txt"
exts = re.findall(r'\.\w+', files)
print("File extensions:", exts)
