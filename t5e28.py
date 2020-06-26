import re
text = "today I have found a lot of material about Earth"
list = re.findall("[ae]\w+", text)
print(list)
