# Chat Seguro - Trabalho de Criptografia e Segurança

## 💻 **Objetivo**

Desenvolver um **chat seguro** que garanta os pilares de **confidencialidade** e **integridade** das mensagens trocadas entre os usuários. Este trabalho visa aplicar conceitos de criptografia simétrica, assimétrica e funções de hash aprendidos em sala de aula.

---

## 🔒 **Descrição do Trabalho**

O trabalho consiste em implementar um sistema de **chat seguro**, utilizando técnicas de criptografia para garantir a segurança da comunicação entre os usuários. A aplicação deve garantir que:

- **Confidencialidade**: As mensagens enviadas devem ser criptografadas antes de serem transmitidas, utilizando criptografia simétrica (AES) e/ou assimétrica (RSA).
- **Integridade**: Implementação de um mecanismo para garantir que as mensagens não foram alteradas durante a transmissão, utilizando funções hash (SHA-256) ou HMAC.

Além disso, será implementado um mecanismo de **autenticação** entre os usuários utilizando **certificados digitais** ou **assinaturas digitais**.

---

## 📑 **Requisitos do Sistema**

### **Confidencialidade**

- As mensagens devem ser criptografadas antes de serem enviadas.
- Uso de **criptografia simétrica** (AES, ChaCha20) ou **assimétrica** (RSA, ECC) será utilizado e justificado na documentação.

### **Integridade**

- Implementação de um mecanismo para garantir que as mensagens não foram alteradas durante a transmissão.
- Uso de **funções hash** (SHA-256, SHA-3) ou **HMAC** para garantir a integridade.

### **Autenticação**

- Implementação de um método de autenticação entre os usuários, utilizando **certificados digitais** ou **assinaturas digitais**.

---

## 🖥️ **Estrutura do Chat**

A estrutura do chat será implementada da seguinte forma:

- **Interface simples**: A interface será desenvolvida em modo texto, mas pode ser expandida para uma interface gráfica usando bibliotecas como **PyQt**.
- **Suporte a múltiplos usuários**: A comunicação será feita por meio de **socket** em um servidor intermediário, permitindo que múltiplos clientes se conectem e enviem mensagens.
- **Uso de sockets**: A comunicação entre cliente e servidor será feita por meio de **sockets TCP/IP**.

---

## 🔧 **Tecnologias Utilizadas**

- **Linguagem de Programação**: **Python**
  - **Bibliotecas de Criptografia**: **PyCryptodome** (para criptografia simétrica e assimétrica), **cryptography** (para funções hash e assinaturas digitais).
  - **Sockets**: Para a comunicação entre cliente e servidor.

---

## 🛠️ **Funcionalidade do Sistema**

### **Funcionamento Básico**:

1. O **cliente** se conecta ao **servidor**.
2. O **servidor** gera a chave pública e privada e a distribui para os clientes.
3. O **cliente** envia uma mensagem criptografada ao servidor.
4. O servidor recebe a mensagem, descriptografa e verifica sua integridade.
5. O **cliente** recebe a resposta do servidor.

**Exemplo de Fluxo de Comunicação**:

- **Cliente → Servidor**: Envia a mensagem criptografada junto com a chave secreta criptografada.
- **Servidor → Cliente**: Envia uma resposta confirmando o recebimento da mensagem.

### **Criptografia e Autenticação**:

- **Criptografia Simétrica (AES)**: Usada para criptografar e descriptografar mensagens.
- **Criptografia Assimétrica (RSA)**: Usada para criptografar a chave secreta enviada pelo cliente.
- **Função Hash (SHA-256)**: Usada para garantir a integridade das mensagens.

---

## 📝 **Testes Realizados**

### **Testes de Funcionalidade**:

- Testamos a criptografia e a descriptografia das mensagens, garantindo que elas sejam transmitidas de forma segura.
- Testamos a verificação de integridade das mensagens usando funções hash.
- Verificamos o fluxo de comunicação entre cliente e servidor.

### **Testes de Segurança**:

- A comunicação entre os clientes e o servidor foi analisada para garantir que não ocorrem vazamentos de informações.
- A validade da assinatura digital foi verificada com sucesso.

---

## 📜 **Conclusões**

### **Pontos Positivos**:

- A implementação da criptografia simétrica e assimétrica proporcionou a **confidencialidade** das mensagens.
- O uso de funções hash (SHA-256) garantiu que as mensagens não fossem alteradas durante o envio.
- O sistema de **autenticação** entre os usuários foi efetivo, garantindo que as mensagens fossem enviadas apenas por usuários válidos.

---

## 🚀 **Como Executar**

### **1. Configuração do Ambiente**:

- Certifique-se de ter o Python instalado.
- Instale as dependências com o seguinte comando:

```bash
pip install pycryptodome cryptography
```

### **2. Gerar as Chaves**:
```bash
python gerar_chaves.py
```

### **2. Iniciar o Servidor:**:
```bash
python server.py
```
### **3. Iniciar o Cliente:**:
```bash
python client.py
```


### Explicação do README:

1. **Objetivo**: Apresenta de forma resumida o que foi feito no trabalho, que é criar um chat seguro.
2. **Descrição do Trabalho**: Explica os requisitos do sistema, como confidencialidade, integridade, criptografia e autenticação.
3. **Tecnologias e Ferramentas**: Detalha as tecnologias utilizadas, como Python e as bibliotecas `PyCryptodome` e `cryptography`.
4. **Como Executar**: Explica os passos para rodar o sistema, como instalar dependências e gerar as chaves.
5. **Testes e Conclusões**: Descreve os testes realizados para garantir que o chat funciona corretamente e de forma segura.
6. **Critérios de Avaliação**: Explica como o trabalho será avaliado com base nos pontos mencionados.
###
⚠️ **Obs:** O **Chat GPT** Foi utilizado nesse trabalho somente para Criar esse **README** E Comentar o codigo para ficar de Facil Entendimento!
