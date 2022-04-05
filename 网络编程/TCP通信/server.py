
import socket
from socket import *
#服务端

def main():
    # AF_INET使用ipv4通信，sock_stream使用tcp通信
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口host不写就是自己
    tcp_server_socket.bind(('', 8999))
    # 允许多少人同时连接我
    tcp_server_socket.listen(128)
    print("[+] 开始监听...")
    # 循环为多个客户服务多次
    while True:
        # 等待用户连接，保护用户的socket和ip
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("[+] The %s:%s connecting" % (str(client_addr[0]), str(client_addr[1])))
        # 给客户发送信息
        new_client_socket.send('Welcome'.encode('utf-8'))
        # 循环为一个客户服务
        while True:
            try:
                # 接受客户发来的数据
                recv_data = new_client_socket.recv(1024)
                if recv_data:
                    print(recv_data.decode('utf-8'))
                else:
                    print("[-] 断开连接")
                    break
            except:
                print('[-] 断开连接')
                break
        # 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()


# ##基本操作
# s = socket()
# host = gethostname()  # 获取自己ip
# print(host)
# port = 12345  # 一会用12345端口通信
# s.bind((host, port))  # 绑定ip和端口
# s.listen(5)  # 等待用户连接，最大5人连接
# print('[+] 开始监听连接...')
# c, addr = s.accept()  # 建立和客户端的连接 c=对方的套接字；addr=对方的ip地址和对方端口以元组形式存在
# print('[+] 成功建立连接')
# print("对方ip地址：",addr)
# c.send('Welcome'.encode("utf-8"))  # 通过客户的套接字发送welcome给对方，utf-8编码
# print(c.recv(1024).decode("utf-8"))  # 接收客户信息
#
# c.close()

    pass


if __name__ == '__main__':
    main()