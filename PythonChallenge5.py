"""
use pickle to restore from saved file to get a object.
it's a quite convenient way to communicate between programs.
"""
import pickle
from urllib import request
with request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as f:
    obj = pickle.load(f)
print(obj)
for line in obj:
    print(''.join(item[0] * item[1] for item in line))