
import socket
from socket import *
#客户端

def main():
    tcp_socket=socket(AF_INET,SOCK_STREAM)
    server_ip = '192.168.183.128'
    server_port =8999
    server_add=(server_ip,server_port)
    #连接服务器
    tcp_socket.connect(server_add)
    print('[+] 连接成功 ')
    #接收第一次发来的数据
    first_data=tcp_socket.recv(1024)
    print(first_data.decode('utf-8'))
    while True:
        #持续发送数据
        send_data=input('Send >> ')
        tcp_socket.send(send_data.encode('utf-8'))
    tcp_socket.close()
        
    
    






# #基操
# s=socket()
# host='192.168.183.128' #你要连接谁的ip
# port=12345
# s.connect((host,port)) #连接服务端
# msg=input("发送： ")
# s.send(msg.encode('utf-8')) #发送信息
# print(s.recv(1024).decode('utf-8')) #接受信息
# s.close()

    pass


if __name__ == '__main__':
    main()