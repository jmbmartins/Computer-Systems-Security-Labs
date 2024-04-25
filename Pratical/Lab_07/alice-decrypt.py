import sys
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from ecc import ECPoint

def calculate_shared_key(point, scalar):
    return point.multiplyPointByScalar(scalar)

def calculate_hash(message):
    hash = SHA256.new()
    hash.update(message.encode())
    return hash.digest()

def decrypt(ciphertext, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    return aes_cipher.decrypt(ciphertext)

def main():
    filename = sys.argv[1]
    sk = int(sys.argv[2], 16)
    G = ECPoint(int(sys.argv[3], 16), int(sys.argv[4], 16))
    Y = ECPoint(int(sys.argv[5], 16), int(sys.argv[6], 16))

    with open(filename, 'rb') as file:
        ciphertext = file.read()

    shared_key = calculate_shared_key(Y, sk)
    hash_value = calculate_hash(str(shared_key.x) + str(shared_key.y))
    message = decrypt(ciphertext, hash_value, os.urandom(16))

    with open('decrypted.txt', 'w') as file:
        file.write(message)

    print("--- BEGIN DECRYPTED MESSAGE ---")
    print(message)

if __name__ == "__main__":
    main()
