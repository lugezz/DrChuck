import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print(type(tree))
print(tree)
print('Name:', tree.find('name').text)
email = tree.find('email')
print("Email: ", email)
print('Email attr:', email.get('hide'))
