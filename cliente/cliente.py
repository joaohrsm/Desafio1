import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))

try:
    while True:
        # Enviando uma mensagem para o servidor
        message = input("Digite uma mensagem para o servidor (ou 'sair' para encerrar): ")
        client_socket.sendall(message.encode())

        # Verifica se a mensagem é de encerramento
        if message.lower() == 'sair':
            break

        # Recebendo resposta do servidor
        try:
            data = client_socket.recv(1024)
            if not data:
                print("O servidor fechou a conexão.")
                break
            print(f"Resposta do servidor: {data.decode()}")
        except ConnectionResetError:
            print("Erro de conexão. O servidor pode ter fechado a conexão.")
            break
finally:
    client_socket.close()
