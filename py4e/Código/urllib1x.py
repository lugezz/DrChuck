from urllib import request

fhand = request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

print("=" * 100)

fhand = request.urlopen('http://dr-chuck.com/page1.html')
for line in fhand:
    print(line.decode().strip())
