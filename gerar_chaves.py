from Crypto.PublicKey import RSA

# Função para gerar chaves pública e privada RSA
def gerar_chaves():
    chave = RSA.generate(2048)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()

    # Salvando as chaves em arquivos
    with open("private.pem", "wb") as private_file:
        private_file.write(chave_privada)

    with open("public.pem", "wb") as public_file:
        public_file.write(chave_publica)

    print("Chaves RSA geradas e salvas com sucesso!")

# Gerar e salvar as chaves
if __name__ == "__main__":
    gerar_chaves()
