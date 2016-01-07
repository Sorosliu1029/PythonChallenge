"""
the content is still in the html source code
mainly use regular expression to meet the command
notice that EXACTLY word
"""
from urllib import request
import re
with request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as f:
    data = f.read().decode('utf-8')
data = ''.join(data.split('\n'))
content = re.findall(r'(<!\-\-.*?\-\->)', data)[0].strip('<!-->')
small_letters = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', content)
print(''.join(small_letters))