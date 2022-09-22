import email
import re

data = 'From: eugenio.vazquez@emissary.ai Sat Jun 5 09:14:16 2022'

# Try to get emissary.ai

# 1) Basic
start = data.find('@')
end = data.find(' ', start)

domain = data[start+1:end]
print(domain)

# 2) Basic2

words = data.split()
email = words[1]
split2 = email.split('@')

domain = split2[1]
print(domain)

# 3) Regex
domain = re.findall('@([^ ]*)', data)
print(domain)
