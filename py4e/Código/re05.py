import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# Parenthesis marks the begin and the end of the extraction
lst = re.findall('from (\S+@\S+)', s)
print(lst)
