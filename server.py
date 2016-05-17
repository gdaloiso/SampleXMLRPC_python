#!/usr/bin/python3.4

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler,
                            allow_none=True)

def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def diff_function(x,y):
    return x - y
server.register_function(diff_function, 'diff')

def ls(dir_name):
    return os.listdir(dir_name)
server.register_function(ls)

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')