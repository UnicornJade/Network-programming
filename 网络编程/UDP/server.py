"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket

def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',6000))
    while True:
        data,addr=s.recvfrom(1024)
        print('[+] Connected by ',addr)
        print('[+] Recv data: ',data)
        s.sendto(data,addr)
    s.close()
    pass
    
    
if __name__ == '__main__':
    main()