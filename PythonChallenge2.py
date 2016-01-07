"""
use a dictionary to count appearance number of different characters
and find the least ones
use urllib to get the html source file
use re to get the target content
"""
from urllib import request
import re
with request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as f:
    data = f.read().decode('utf-8')
data = ''.join(data.split('\n'))
content = re.findall(r'(<!\-\-.*?\-\->)', data)[1].strip('<!-->')
counter = {}
for char in content:
    counter[char] = counter.get(char, 0) + 1
print(''.join([char for char in content if counter[char] == 1]))