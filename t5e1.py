import re
def allowedcharacters(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(allowedcharacters("ABCDEFabcdef123450")) 
print(allowedcharacters("*&%@#!}{"))