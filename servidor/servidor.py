import socket

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Servidor escutando na porta 12345...")

# Função para gerar resposta personalizada com base na mensagem recebida
def generate_response(message):
    if "olá" in message.lower():
        return "Olá! Como posso ajudar você hoje?"
    elif "tempo" in message.lower():
        return "Hoje o tempo está ensolarado!"
    elif "ajuda" in message.lower():
        return "Claro! O que você precisa?"
    else:
        return "Desculpe, não entendi sua mensagem."

# Aceitando conexões de clientes
while True:
    conn, addr = server_socket.accept()
    print(f"Conectado por {addr}")

    while True:
        # Recebendo mensagem do cliente
        data = conn.recv(1024)
        if not data:
            print("Cliente desconectado.")
            break

        message = data.decode()
        print(f"Mensagem recebida: {message}")

        # Verifica se a mensagem é de encerramento
        if message.lower() == 'sair':
            print("Mensagem de encerramento recebida. Encerrando conexão.")
            break

        # Gerando uma resposta personalizada
        response = generate_response(message)

        # Respondendo ao cliente
        conn.sendall(response.encode())

    conn.close()
