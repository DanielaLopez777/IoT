import socket

# Crear un socket para el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a una dirección IP y puerto
server_socket.bind(("127.0.0.1", 1234))

# Escuchar conexiones entrantes
server_socket.listen()

    # Aceptar conexiones
    client_socket, client_address = server_socket.accept()

    # Recibir datos del cliente
    data = client_socket.recv(1024)

    # Enviar datos de vuelta al cliente
    client_socket.sendall(data)

    # Cerrar la conexión con el cliente
    client_socket.close()while True:
