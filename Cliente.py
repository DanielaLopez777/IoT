import socket

# Crear un socket para el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket a una dirección IP y puerto
client_socket.connect(("192.168.0.111", 1234))

# Enviar datos al servidor
client_socket.sendall(b"Hola Servidor soy el cliente")

# Recibir datos del servidor
data = client_socket.recv(1024)

# Imprimir los datos recibidos
print("Received:", data)

# Cerrar la conexión con el servidor
client_socket.close()
