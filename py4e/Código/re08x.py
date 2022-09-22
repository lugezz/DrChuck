# Search for lines that have an at sign between characters
# The characters must be a letter or number
# The results will be slightly more accurate than re07.py for email addresses
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
