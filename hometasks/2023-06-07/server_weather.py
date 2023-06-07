import socket
import threading
import requests
from config import url, key


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 123

server_socket.bind((host, port))
print(f'Server runs at {host}, port {port}')

server_socket.listen(5)


def handle_client(client_socket, client_address):
    print(f'Client connected: {client_address}')
    message = 'Welcome! You are connected to weather server'
    client_socket.send(message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print(f'Client {client_address} disconnected')
            break

        city = client_message.strip()
        try:
            params = {'APPID': key, 'q': city, 'units': 'metric'}
            result = requests.get(url, params=params)
            data = result.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"]

            descr_dict = {'clear sky': '☀️',
                                'few clouds': '🌤',
                                'scattered clouds': '🌥',
                                'broken clouds': '☁️',
                                'shower rain': '🌧',
                                'rain': '🌦',
                                'thunderstorm': '⛈',
                                'snow': '❄️',
                                'mist': '🌫'}

            answer = f'current weather in {city}'.upper().center(50, '=') + "\n" \
                     f'{"=" * 50}\n' \
                     f'Temperature: {temp}°C\n' \
                     f'Description: {description} {descr_dict[description] if description in descr_dict else ""}\n' \
                     f'Humidity: {humidity}%\n' \
                     f'Pressure: {pressure}mm\n' \
                     f'Wind: {wind}m/s\n'
        except Exception as e:
            answer = f'An error ({e}) occurred when trying to retrieve data'

        client_socket.send(answer.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()


