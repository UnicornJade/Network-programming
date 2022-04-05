"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket

def send_msg(udp_socket):
    #获取发送内容
    dest_ip=input('请输入对方ip: ')
    dest_port=int(input('请输入对方端口: '))
    send_data=input('你想说啥: ')
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip,dest_port))

def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    print('%s 说了 %s'%(str(recv_data[1]),recv_data[0].decode('utf-8')))



def main():
    #创建UDP套接字
    udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #绑定信息
    udp_socket.bind(('',7788))
    while True:
        send_msg(udp_socket)
        recv_msg(udp_socket)
    
    pass
    
    
if __name__ == '__main__':
    main()