import re

#f = open("newfile.txt", "r")
#text = f.read()
#list = re.findall('[0-9]+',text)
#print(list)
#sum = sum([int(value) for value in list])
#print(sum)

sum = sum([int(value) for value in re.findall('[0-9]+',open("newfile.txt", "r").read())])
print(sum)
