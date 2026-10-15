import re

text = "Visit http://example.com or https://openai.com"
urls = re.findall(r'https?://\S+', text)
print("Web addresses:", urls)
