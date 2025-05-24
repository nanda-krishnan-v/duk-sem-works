import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from: {addr}")
    
    request = client_socket.recv(1024).decode()
    if request == "TIME":
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_socket.send(current_time.encode())
    else:
        client_socket.send(b"Invalid request")
    
    client_socket.close()
