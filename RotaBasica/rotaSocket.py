import socket

def rotas(data):
    # Verifica qual rota foi requisitada
    if "GET /hello" in data:
        return "HTTP/1.1 200 OK\nConnection: close\n\nOla, mundo!"
    elif "GET /status" in data:
        return "HTTP/1.1 200 OK\nConnection: close\n\nServidor ativo e rodando!"
    else:
        return "HTTP/1.1 404 Not Found\nConnection: close\n\nRota nao encontrada"

# Cria o Socket TCP

host = "localhost"
porta = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, porta))
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    print(f"conexão aceita na porta {porta}...")

    data = conn.recv(1024).decode('utf-8')
    print("Dados recebidos:", data)

    # Chama a função que decide a resposta com base na rota
    response = rotas(data)
    conn.sendall(response.encode('utf-8'))

    conn.close()
