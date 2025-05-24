import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = 'localhost'
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server listening on {host}:{port}...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from client
data = conn.recv(1024).decode()
print(f"Received from client: {data}")

# Send acknowledgment
ack_message = "Server received your message."
conn.send(ack_message.encode())

conn.close()
