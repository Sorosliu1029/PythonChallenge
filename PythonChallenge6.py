"""
based on the channel.zip
try to follow the instruction and collect the comment
the comment is the key
"""
from zipfile import ZipFile
import re
z = ZipFile('channel.zip')
print(ZipFile.read(z, 'readme.txt').decode('utf-8'))
number = '90052'
comment = ''
re_number = re.compile(r'nothing is (\d+)$')
while number:
    content = ZipFile.read(z, number + '.txt').decode('utf-8')
    comment += ZipFile.getinfo(z, number + '.txt').comment.decode('utf-8')
    try:
        number = re_number.findall(content)[0]
        print(number)
    except IndexError:
        print(content)
        break
print(comment)
# oxygen
# there is still a riddle hide in the comment
