'''
ip：计算机网络的唯一地址
端口号：区分同一台计算机不同应用程序
'''
'''
socket模块：服务于网络通信的标准库
socket函数：创建套接字的函数
套接字：
            打电话             VS              网络通信
            信号的传输规则                     TCP/IP协议
            电话号码                           IP地址+端口号
            电话机                             套接字
'''
import socket
s=socket.socket(socket.AF_INET,                           socket.SOCK_STREAM)#套接字的创建
            #AF_INET表示IPV4地址，AF_INET6表示IPV6地址    #使用TCP协议

#服务器端
ip=socket.gethostname()
port=9002
s.bind((ip,port))#把元组地址绑定给套接字
s.listen(5)#对套接字进行监听,参量为最多监听的个数
#s.accept()#会导致程序暂停，一直到请求到来为止

#new_s新的套接字，建立连接后进行交流
#addr对方的地址，ip+端口号的元组形式
new_s,addr=s.accept()

'''
        客户端                         服务器端
        发起连接请求                  接受连接请求，并建立连接    
       
'''
#客户端
user=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_user=socket.gethostname()
port_user=9002
user.connect((ip_user,port_user))

#发送-----服务器端

msg = 'connect success'
new_s.send(msg.encode('utf-8'))#不管这个msg是什么汉字编码格式，都统一为utf-8汉字格式

#接收------客户端
msg=s.recv(1024)
print(msg.decode('utf-8'))#解码

#先运行服务器端的代码，再运行客户端的代码



