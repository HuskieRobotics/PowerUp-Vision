#creates and sends json packets with socket

import socket
import sys
import time
import json

class Client:
    def __init__(self, HOST,PORT):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.HOST = HOST
        self.PORT = PORT
    def sendData(self,list_args):
        sock.sendto(createJSON(list_args),(self.HOST,self.PORT))
    def createJSON(self,list_args):
        return json.dumps(list_args)

        
