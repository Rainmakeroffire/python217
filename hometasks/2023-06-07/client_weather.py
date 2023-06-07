import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 123

client_socket.connect((host, port))

server_message = client_socket.recv(1024).decode()
print(server_message)

while True:
    client_message = input(f'Enter a city name: ')
    print()
    client_socket.send(client_message.encode())

    if not client_message:
        print('Disconnecting')
        break

    server_response = client_socket.recv(1024).decode()
    print(f'Server response:\n\n{server_response}\n')

client_socket.close()
