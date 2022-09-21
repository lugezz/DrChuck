import re

x = 'From: Artime who is: good and crazy'
y = re.findall('^F.+:', x)
# Found the longer possible result
print('Result found:', y)

y = re.findall('^F.+?:', x)
# ? sign make it found the shorter possible result
print('Result found:', y)

