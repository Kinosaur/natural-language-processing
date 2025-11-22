import re

text = "I have so much fun. Yahoo! kwan@scitech.com"

email_regex = '[a-zA-Z0-9_]+[a-zA-Z0-9_.]*@[a-zA-Z0-9]+.[a-zA-Z0-9]+'
cleaned_text = re.sub(email_regex, '', text)
print(cleaned_text)

words = cleaned_text.split()
print(words)

emails = re.findall(email_regex, text)
print(emails)
