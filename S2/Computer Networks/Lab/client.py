import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

# Connect to server
client_socket.connect((host, port))

# Send message to server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive acknowledgment from server
data = client_socket.recv(1024).decode()
print(f"Received from server: {data}")

# Close the connection
client_socket.close()


