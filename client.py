#!/usr/bin/python3.4
from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:8000')

print(s.add(2,3))  
print(s.diff(2,3))  
print(s.ls('/tmp'))
