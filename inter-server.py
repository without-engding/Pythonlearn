import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 套接字的创建
# AF_INET表示IPV4地址，AF_INET6表示IPV6地址    #使用TCP协议

# 服务器端
ip = socket.gethostname()
port = 9002
s.bind((ip, port))  # 把元组地址绑定给套接字
s.listen(5)  # 对套接字进行监听,参量为最多监听的个数
# s.accept()#会导致程序暂停，一直到请求到来为止

# new_s新的套接字，建立连接后进行交流
# addr对方的地址，ip+端口号的元组形式
new_s, addr = s.accept()


# 发送-----服务器端

msg = 'connect success'
new_s.send(msg.encode('utf-8'))  # 不管这个msg是什么汉字编码格式，都统一为utf-8汉字格式

