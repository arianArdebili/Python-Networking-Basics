import socket

ip = "0.0.0.0"
port = 1234

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
print(f"server is binding with ip: {port}, port: {port} ")

server.listen(5)
print('[+] server is listening ....')

while True:
    client, addr = server.accept()
    print(f'[+] connection accepted from {addr}')

    welcome_message = 'welcome to the server \n'
    client.send(welcome_message.encode('utf-8'))

    client.close()