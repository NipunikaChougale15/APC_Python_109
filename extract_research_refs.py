import re

ref = "DOI:10.1000/xyz123 Published:2020 Email: author@example.com URL: https://journal.org"
doi = re.findall(r'DOI:\s*\S+', ref)
years = re.findall(r'\b\d{4}\b', ref)
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', ref)
urls = re.findall(r'https?://\S+', ref)
print("DOI:", doi, "Years:", years, "Emails:", emails, "URLs:", urls)
