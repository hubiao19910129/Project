import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接服务器
client.connect(("10.150.123.247",8080))

count = 0
while True:
    count  +=1
    data = input("请发送服务器的请求：")

    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务启说：",info.decode("utf-8"))
