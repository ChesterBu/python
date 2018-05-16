import re
import hashlib

string = 'alex36wupeiqi33xialu32'

print(re.search(r'(?P<name>[a-z]+)\d+', string).group('name'))

print(re.search(r'(?P<name>[a-z]+)(?P<age>\d+)', string).group('age'))


obj = hashlib.md5('hahah'.encode('utf8'))

obj.update('hello'.encode('utf-8'))

print(obj.hexdigest())
