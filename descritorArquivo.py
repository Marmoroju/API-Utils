import socket
import os

# 1. Criando o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Obtendo o descritor de arquivo do socket
fd = server_socket.fileno()
print("Descritor de Arquivo no servidor estabelecida no socket com o ID:", fd)

# 3. Associando o socket a um endereço e porta
server_socket.bind(('localhost', 8080))

# 4. Colocando o socket em modo de escuta
server_socket.listen(5)
print("Servidor escutando na porta 8080...")

while True:
    # 5. Aceitando uma conexão
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    # 6. Mostrando o descritor de arquivo da conexão
    print("Descritor da conexão:", conn.fileno())

    # 7. Recebendo dados do cliente
    data = conn.recv(1024).decode('utf-8')
    print("Dados recebidos:", data)

    # 8. Criando resposta simples (API básica)
    response = (    
                "HTTP/1.1 200 OK\n\n"
                "API com sockets e descritor de arquivo funcionando!\n\n"
                f"ID do descritor: {conn.fileno()}\n\n"
                f"Socket: {addr}\n\n"
                "Os navegadores abrem multiplas conexoes para otimizar o carregamento das paginas.\n\n"
                "Pressione F12 > Rede (Cada Nome = uma conexao) > Visualizacao/Resposta (Um socket aberto para cada Nome)"
                )
    conn.sendall(response.encode('utf-8'))

    # 9. Fechando a conexão
    conn.close()