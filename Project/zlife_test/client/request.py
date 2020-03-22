import requests
import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("172.20.21.160",25658))

data = input("::::::::::::::::")
client.send(data.encode("utf-8"))

info = client.recv(1024)
print(info.decode("utf-8"))

client.close()