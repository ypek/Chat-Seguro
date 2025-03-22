import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Função para carregar a chave pública do servidor
def carregar_chave_publica():
    with open("public.pem", "rb") as public_file:
        chave_publica = RSA.import_key(public_file.read())
    return chave_publica

# Função para carregar a chave privada do cliente
def carregar_chave_privada():
    with open("private.pem", "rb") as private_file:
        chave_privada = RSA.import_key(private_file.read())
    return chave_privada

# Função para criptografar mensagens com AES
def criptografar_mensagem(mensagem, chave_secreta):
    cipher = AES.new(chave_secreta, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(mensagem.encode())
    return nonce + tag + ciphertext

# Função para criptografar a chave secreta com RSA
def criptografar_chave_secreta(chave_secreta, chave_publica):
    cipher_rsa = PKCS1_OAEP.new(chave_publica)
    chave_secreta_criptografada = cipher_rsa.encrypt(chave_secreta)
    return chave_secreta_criptografada

# Função para enviar mensagem ao servidor
def enviar_mensagem(host, port, mensagem):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    chave_secreta = get_random_bytes(16)  # Gerando chave secreta para a criptografia
    chave_publica = carregar_chave_publica()

    # Criptografar a chave secreta com a chave pública do servidor
    chave_secreta_criptografada = criptografar_chave_secreta(chave_secreta, chave_publica)
    client_socket.send(chave_secreta_criptografada)  # Enviando a chave secreta criptografada

    # Agora, criptografamos a mensagem com a chave secreta
    mensagem_criptografada = criptografar_mensagem(mensagem, chave_secreta)

    # Envia a mensagem criptografada
    client_socket.send(mensagem_criptografada)

    resposta = client_socket.recv(1024)
    print(f"Resposta do servidor: {resposta.decode()}")

    client_socket.close()

# Rodando o cliente
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    while True:
        # Pedir a mensagem para o usuário
        mensagem = input("[*]Digite a Mensagem a ser encaminhada para o servidor (ou 'sair' para encerrar): ")
        
        if mensagem.lower() == 'sair':
            print("Saindo do chat.")
            break
        
        # Enviar a mensagem para o servidor
        enviar_mensagem(host, port, mensagem)
