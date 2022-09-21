import re

x = 'my 2 favourites numbers are 19 and 421'
y = re.findall('[0-9]+', x)
print('Number one one more digits found:', y)

y = re.findall('[AEIOU]', x)
print('Uppercase vowels:', y)

y = re.findall('[aeiou]', x)
print('Lowercase vowels:', y)
