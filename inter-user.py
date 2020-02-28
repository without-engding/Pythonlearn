import socket


'''
        客户端                         服务器端
        发起连接请求                  接受连接请求，并建立连接    

'''
# 客户端
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_user = socket.gethostname()
port_user = 9002
user.connect((ip_user, port_user))


# 接收------客户端
msg = user.recv(1024)
print(msg.decode('utf-8'))  # 解码

# 先运行服务器端的代码，再运行客户端的代码