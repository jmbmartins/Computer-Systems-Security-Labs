# Cheat Sheet

## Comandos Gerais Linux

- Verificar ficheiro em HEX:
  ~~~console
  $ hexdump -C [nomeficheiro]
  ~~~

- Comprimir um ficheiro:
  ~~~console
  $ zip comprimido.txt texto.txt
  ~~~

- 10 bytes pseudoaleatórios em hexadecimal:
  ~~~console
  $ openssl rand -hex 10
  ~~~

## Comandos Gerais OpenSSL 

- Gera um conjunto de bytes pseudo-aleatórios:
  ~~~console
  $ openssl rand -hex [16] # Gera 16 bytes pseudo-aleatórios em hexadecimal
  ~~~

- Padrão OpenSSL
  ~~~console
  $ openssl <MÉTODO> <FLAGS> <ARGUMENTOS>
  ~~~
  
  - Parâmetros:
    - `-K` Chave em Hexadecimal
    - `-k` Chave em ASCII
    - `-out / -in` Ficheiro de Saída / Ficheiro de Entrada
    - `-in` Ficheiro de Entrada
    - `-e / -d ` Operação de Encriptação / Operação de Decriptação 

---------------------------------------------------------------------------------------

## Cifra de Chave Simétrica Contínua (RC4 - Rivest Cipher 4, ChaCha20)


### Conceitos

**Simétrica**: A mesma chave que é usada para encriptar, é também usada para desencriptar.

**Contínua**: A partir de uma chave com tamanho fixo e comportável, gera uma sequência tão grande quanto necessária para cifrar qualquer ficheiro.

### Fórmula para **encriptar** ficheiro:

~~~console
$ openssl enc -e <ALGORTIMO> -in <ficheiro> -out <criptograma> -K <chave> 
~~~

#### Exemplos:

~~~console
$ openssl enc -e -chacha20 -in plaintext.txt -out ciphertext.cc20 -K abcdef0123456789
~~~
~~~console
$ openssl enc -e -rc4 -in plaintext.txt -out ciphertext.rc4 -K abcdef0123456789
~~~

### Fórmula para **encriptar** ficheiro:

~~~console
$ openssl enc -e <ALGORTIMO> -in <ficheiro> -out <criptograma> -K <chave> 
~~~

#### Exemplos:

~~~console
$ openssl enc -e -chacha20 -in plaintext.txt -out ciphertext.cc20 -K abcdef0123456789
~~~
~~~console
$ openssl enc -e -rc4 -in plaintext.txt -out ciphertext.rc4 -K abcdef0123456789
~~~


### Fórmula para **desencriptar** ficheiro:

~~~console
$ openssl enc -d <ALGORTIMO> -in <criptograma> -out <ficheiro> -K <chave> 
~~~

#### Exemplos:

~~~console
$ openssl enc -d -chacha20 -in ciphertext.cc20 -out textodesencriptado.txt -K abcdef0123456789
~~~
~~~console
$ openssl enc -d -rc4 -in ciphertext.rc4 -out textodesencriptado.txt -K abcdef0123456789
~~~


### Análise

- A melhor para cifrar à medida que os dados são gerados.

- Sofre do problema da **Maneabilidade** (Muito maneável):
  - Caso se sofra um ataque de homem no meio **ativo**, o recetor da mensagem não irá conseguir detatar a alteração.



--------------------------------------------------------------------------
## Cifra de Chave Simétrica Por Blocos (AES - Advanced Encryption Standart , DES, DES3)

### Conceitos

**Simétrica**: A mesma chave que é usada para encriptar, é também usada para desencriptar.

**Blocos**: Aplica uma transformação ao resultado da função anterior até que o bloco de criptograma (ou bloco pseudoaleatório) seja produzido.  

**Extensões**: 
  - AES ECB (Eletronic Code Book): 
    - Cifra cada bloco individualmente com a mesma chave, ou seja, dois blocos iguais vão originar o mesmo criptograma.
    - Padding: Preenchimento do bloco 
        - Exemplo: OLATUDOBEM (10 bytes - faltam 6 para os 16 bytes, logo meter o 6, 6x)  ->  OLATUDOBEM666666.  

  - AES CBC (Cipher Block Chaining):
    - Ciframento incremental.
    - Precisa de um iv (que funciona como bloco anterior ao 1º bloco)
    - Não aguenta processamento paralelo na cifragem, mas na decifragem aguenta.
    - Dá sempre o mesmo criptograma, para qualquer tempo, com qualquer processador.


### Fórmula para **encriptar** ficheiro:

~~~console
$ openssl enc -e <ALGORTIMO> -in <ficheiro> -out <criptograma> -K <chave> -iv <num>
~~~

#### Exemplos:

- AES CBC
~~~console
$ openssl enc -e -aes128-cbc -in texto.txt -out cifrado.cbc -K 0123456789abcdef0123456789abcdef -iv 0 # -iv obrigatório
~~~

- AES ECB
~~~console
$ openssl enc -e -aes128-ecb -in texto.txt -out cifrado.ecb -K 0123456789abcdef0123456789abcdef
~~~

### Fórmula para **desencriptar** ficheiro:

~~~console
$ openssl enc -d <ALGORTIMO> -in <criptograma> -out <ficheiro> -K <chave> -iv <>
~~~

#### Exemplos:

- AES CBC
~~~console
$ openssl enc -d -aes-128-cbc -in ciphertext.cbc -out textodesencriptado.txt -K abcdef0123456789 -iv 1221221
~~~

- AES ECB
~~~console
$ openssl enc -d -aes-128-cbc -in ciphertext.ecb -out textodesencriptado.txt -K abcdef0123456789 
~~~




--------------------------------------------------------------------------
## Funções de Hash Criptográficas (SHA - Secure Hash Algorithm  , MD5 - Message Digest 5)

### Conceitos

- Funções que dado um input qualquer, devolvem um output com tamanho fixo.
- Dado um ficheiro, é muito eficiente calcular o seu valor de HASH.

#### SHA - Secure Hash Algorithm (SHA1 160bits)

~~~console
$ openssl dgst -sha1 [nome_fich]
~~~

#### MD5 - Message Digest 5 (Ron Rivest) (128bits)

~~~console
$ openssl dgst -md5 [nome_fich]
~~~

Propriedades:
  - Resistência ao cálculo de uma pré-imagem: Encontrar o ficheiro que deu origem ao hash.

  - Resistência ao cálculo de uma segunda pré-imagem: Dado um ficheiro e o seu valor de hash, encontrar outro com o mesmo valor.

  - Resistência a colisões: Dois ficheiros terem o mesmo valor de hash


### **MAC** - Message Authentication Code

#### Conceitos:
 - Mecanismo de Integridade que usa chaves simétricas


INPUTS: 
 - (1) Código MAC
 - (2) Chave 
 - (3) Ficheiro

OUTPUT na elaboração: 
 - Código MAC (ficheiro cifrado com o hash do ficheiro enviado).

OUTPUT na verificação: 
 - V / F


####  **Construir** um MAC


1. Calcular o valor de hash para o SHA1 do ficheiro para texto-limpo.sha1
~~~console
$ openssl dgst -sha1 texto-limpo > texto-limpo.sha1
~~~

2. Cifrar o valor de hash com o AES para o ficheiro
~~~console
$ openssl enc -aes128 -e -k 11121212asqwqs -in texto-limpo.sha1 -out texto-limpo.sha1.aes -iv 0 
~~~



####  **Verificar** um MAC


1. Calcular o valor de hash (SHA1) do ficheiro que recebi
~~~console
$ openssl dgst -sha1 texto-limpo.txt
~~~

2. Decifrar o ficheiro "texto-limpo.sha1.aes"
~~~console
$ openssl enc -d -aes128 -k 11121212asqwqs -in texto-limpo.sha1.aes -out texto-limpo.sha1.txt -iv 0
~~~

1. Diferença do hash do ficheiro recebido e do hash do ficheiro desencriptado
~~~console
$ diff arquivo_recebido.sha1 arquivo_recebido.sha1.txt
~~~


#### Garantias

1. O ficheiro não sofreu erros aleatórios durante a transmissão (integridade)
2. O ficheiro não foi alterado, intencionalmente, durante a transmissão (autenticação da origem da informação)


### **HMAC** - Hash Message Authentication Code

1. Criar:
~~~console
$ openssl dgst -sha256 -hmac <key> textolimpo.txt > textolimpo.hmac
~~~
~~~console
$ openssl dgst -sha256 -hmac "key" textolimpo.txt > textolimpo.hmac
~~~



2. Verificar (Fazer o HMAC do ficheiro recebido e comparar o ficheiro .mac recebido - Recebemos fichNormal, fichMAC)
~~~console
1)
$ openssl dgst -sha256 -hmac "key" fichNormal.txt > textoTXTRecebido.mac

2)
$ diff textoTXTRecebido.mac  fichmac.mac
~~~




---------------------------------------------------------------------------------------

## Cifra de Chave Pública (RSA - Rivest Shamir Adleman)

Uma cifra de chave pública tem:
  - gerador de chaves (pk, sk)
  - algoritmo para cifrar 
  - algoritmo para decifrar


### **Gerar** Par Chaves Aleatórias




~~~console
$ openssl genrsa -out <fich_chave> <tam_chave>
~~~

Exemplo 1:
~~~console
$ openssl genrsa -out sk-and-pk.pem 2048
~~~


Exemplo 2:
~~~console
$ openssl genrsa -aes256 -out sk-and-pk.pem 2048
~~~






### **Extrair** Chave Pública

~~~console
$ openssl rsa -in <fich_chave> -pubout -out <pk_NomeFich.pem> 
~~~


~~~console
$ openssl rsa -in sk-and-pk.pem -pubout -out pk_Joao.pem 
~~~



### **Cifrar** com Chave **Pública**

~~~console
$ openssl rsautl -encrypt -pubin -inkey <ficheiro_chave_publica> -in <ficheiro> -out <ficheiro_cifrado.rsa>
~~~

### **Decifrar** com Chave **Privada**

~~~console
$ openssl rsautl -decrypt -inkey <chave_privada.pem> -in <ficheiro_cifrado.rsa> -out <ficheiro_decifrado>
~~~



### PGP - Pretty Good Privacy (Cifrar com AES utilizando chaves públicas)


### **Cifrar**

1. Gerar chave para usar no AES - secret.key
~~~console
$ cat <fichkeyg.txt> > secret.key
~~~

2. Cifrar ficheiro com AES 
~~~console
$ openssl enc -e -aes128 -in <fich.txt> -out <fich.aes> -K secret.key
~~~

1. Cifrar ficheiro que contém a secret.key com RSA
~~~console
$ openssl rsault -encrypt -pubin -inkey pk.Colega.pem -in secret.key -out secret.key.rsa
~~~


### **Decifrar**

1. Decifrar ficheiro que contém a secret.key com RSA
~~~console
$ openssl rsa -decrypt -inkey sk_and_pk.pem -in secret.key.rsa -out secret.key2
~~~

2. Decifrar ficheiro com AES 
~~~console
$ openssl enc -d -aes128 -in <fich.aes> -out <fich.txt> -K secret.key2
~~~



---------------------------------------------------------------------------------------
## Assinatura Digital


Um esquema de assinatura digital recorrendo a chaves públicas (nomeadamente RSA), faz uso de três algoritmos:
1. Gerar chaves RSA.
2. t = RSA(private, SHA256(m))  m,t
3. m,t, pública
   1. hash = RSA(publica, t)
   2. SHA256(m) = hash ?
      1. Se sim, verifica
      2. Se não, não verifica


### Assinar 




~~~console
$ openssl dgst -sha256 -sign privatekey.pem -out signature.sign file.txt
~~~


Example:

~~~console
$ openssl dgst -sha256 -sign sk-and-pk.pem -out noticias.sig noticias.txt
~~~



### Verificar Assinatura


~~~console
$ openssl dgst -sha256 -verify publickey.pem -signature signature.sign file.txt
~~~

Example:
~~~console
$ openssl dgst -sha256 -verify pk.pem -signature noticias.sig noticias.txt
~~~


--------------------------------------------------------------------------------
## Derivação de Chaves de Cifra

### Representação de Passwords
*root:$1$hODZpn2J$fffGRrpV6O/8tF2XuCSrM1*:
  1. *root* - utilizador.
  2. *$1* - indica que está a ser usado o algoritmo 1 para tratamento e armazenamento da password (algooritmo baseado no *hash* MD5)).
  3. *$hODZpn2J$* - *salt* utilizado.
  4. *$fffGRrpV6O/8tF2XuCSrM1$* - valor que o sistema operativo guarda da password.

#### Exemplo: Criar a representação da password *supermancom* o *salt* *LoisLane*
- `openssl passwd -6 -salt LoisLan superman`

--------------------------------------------------------------------------------
## Teste de Comunicações TLS

### Estabelecer Ligação com o Site da Google
`openssl s_client -tls1_3 www.google.com:443 `

#### Indica a Localização dos Certificados de Raiz:
`openssl s_client -connect www.ubi.pt:443 -CApath /etc/ssl2/`

### Fazer Pedidos *HTTP* a Sites
1. `openssl s_client -connect www.ubi.pt:433`
2. ```
   GET /Default.aspx HTTP/1.1
    Host: www.ubi.pt ```

3. Ver mensagens trocadas: `openssl s_client -connect www.ubi.pt:443 -tls1_2 -msg`


### Simular Sevidor TLS

1. Correr Servidor:
`openssl s_server -nocert -cipher ADH:@SECLEVEL=0`

2. Conectar-se ao Servidor:
`openssl s_client -connect localhost -cipher ADH:@SECLEVEL=0`

3. Criar certificado no ficheiro `server.pem` e guarda as chaves *RSA* em `serverkey.pem`
`openssl req -new -x509 -extensions v3_ca -keyout serverkey.pem -out server.pem -days 1825`

4. Atribuir certificado a página *HTML*:
`openssl s_server -cert server.pem -key serverkey.pem -WWW index.html`









