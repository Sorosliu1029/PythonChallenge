"""
simply use urllib to repeatedly get source text and update the request
printing out the iteration result is a good choice
"""
from urllib import request
import re
nothing = 12345
while nothing:
    with request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % nothing) as f:
        content = f.read().decode('utf-8')
    try:
        nothing = int(re.findall(r'and the next nothing is (\d+)$', content)[0])
        print(nothing)
    except IndexError:
        if 'Divide by two' in content:
            nothing >>= 1
            continue
        elif 'html' in content:
            print(content)
            break

