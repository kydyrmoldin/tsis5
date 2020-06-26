import re
text=input()
print(re.findall(r"\b\w{5}\b", text))
