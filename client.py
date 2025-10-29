import socket

ip =  "127.0.0.1"
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

#recive the message
message = client.recv(1024).decode('utf-8')

print(f'[Server]: {message}')
client.close()