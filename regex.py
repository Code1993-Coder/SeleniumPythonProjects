import re

text = "Contact us at support@example.com or sales@example.org for more info."

# Simple regex for email extraction
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print(emails)


var=text.split("at")[1].strip().split(" ")[0]

print(var)
