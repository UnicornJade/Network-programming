"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket
from socket import *
def main():
    s=socket(AF_INET,SOCK_STREAM)
    host='192.168.183.128'
    port=12345
    s.connect((host,port))

    while True:
        data_recv=s.recv(1024)
        print(data_recv.decode('utf-8'))
        msg=input(">> ")
        s.send(msg.encode('utf-8'))
    s.close()
    
    pass
    
    
if __name__ == '__main__':
    main()