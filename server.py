import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# Função para carregar a chave pública do servidor
def carregar_chave_publica():
    with open("public.pem", "rb") as public_file:
        chave_publica = RSA.import_key(public_file.read())
    return chave_publica

# Função para carregar a chave privada do servidor
def carregar_chave_privada():
    with open("private.pem", "rb") as private_file:
        chave_privada = RSA.import_key(private_file.read())
    return chave_privada

# Função para descriptografar a chave secreta com RSA
def descriptografar_chave_secreta(chave_secreta_criptografada, chave_privada):
    cipher_rsa = PKCS1_OAEP.new(chave_privada)
    chave_secreta = cipher_rsa.decrypt(chave_secreta_criptografada)
    return chave_secreta

# Função para descriptografar mensagens com AES
def descriptografar_mensagem(mensagem_criptografada, chave_secreta):
    nonce, tag, ciphertext = mensagem_criptografada[:16], mensagem_criptografada[16:32], mensagem_criptografada[32:]
    cipher = AES.new(chave_secreta, AES.MODE_EAX, nonce=nonce)
    mensagem = cipher.decrypt_and_verify(ciphertext, tag)
    return mensagem.decode()

# Função para assinar uma mensagem
def assinar_mensagem(chave_privada, mensagem):
    h = SHA256.new(mensagem.encode())
    assinatura = pkcs1_15.new(chave_privada).sign(h)
    return assinatura

# Função para formatar e exibir as mensagens
def formatar_mensagem(mensagem):
    # Emojis e formatação simples para facilitar a leitura
    mensagem_formatada = f"\n\n💬 Mensagem recebida: {mensagem}\n"
    mensagem_formatada += "-------------------------------------------"
    return mensagem_formatada

# Função para lidar com a comunicação de cada cliente
def handle_client(client_socket):
    chave_privada = carregar_chave_privada()

    # Recebe a chave secreta criptografada
    chave_secreta_criptografada = client_socket.recv(256)  # Supondo que o tamanho da chave RSA seja 256 bytes
    chave_secreta = descriptografar_chave_secreta(chave_secreta_criptografada, chave_privada)

    while True:
        # Recebe a mensagem criptografada
        mensagem_criptografada = client_socket.recv(1024)
        if not mensagem_criptografada:
            break

        try:
            mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, chave_secreta)

            # Exibindo a mensagem formatada com emoji e quebra de linha
            print(formatar_mensagem(mensagem_descriptografada))

            # Assinando a mensagem recebida
            assinatura = assinar_mensagem(chave_privada, mensagem_descriptografada)
            print(f"🔐 Assinatura gerada: {assinatura.hex()}")

            # Envia resposta ao cliente
            client_socket.send("✅ Mensagem recebida com sucesso.".encode())
        except ValueError:
            print("❌ Erro de autenticação na mensagem recebida!")

    client_socket.close()

# Função para iniciar o servidor e escutar as conexões
def iniciar_servidor(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor rodando em {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"🔗 Conexão estabelecida com {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Rodando o servidor
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    iniciar_servidor(host, port)
