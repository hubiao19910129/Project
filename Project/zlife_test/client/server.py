import socket

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定IP端口
server.bind(("10.150.123.247",8080))

#监听
server.listen(5)
print("服务启动成功.......")

#等待连接
clientSocket,clientAddress = server.accept()
print("%s ---- %s 连接成功"%(str(clientSocket),clientAddress))

while True:

    data = clientSocket.recv(1024)
    #decode是将编码数据解码成unicode的str字符串
    print("收到的数据："+data.decode("utf-8"))
    #encode是将unicode的str字符串编码，因为计算机不能直接传输字符串
    clientSocket.send("有来无往非礼也".encode("utf-8"))



