import re

post = "Loving #Python #Coding #AI"
hashtags = re.findall(r'#\w+', post)
print("Hashtags:", hashtags)
