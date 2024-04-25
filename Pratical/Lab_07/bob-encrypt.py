import sys
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import binascii
from ecc import ECPoint

def generate_random_number():
    rnd = Random.new()
    return int(binascii.hexlify(rnd.read(24)), 16)

def calculate_shared_key(point, scalar):
    return point.multiplyPointByScalar(scalar)

def calculate_hash(message):
    hash = SHA256.new()
    hash.update(message.encode())
    return hash.digest()

def encrypt(message, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    return aes_cipher.encrypt(message)

def main():
    filename = sys.argv[1]
    G = ECPoint(int(sys.argv[2], 16), int(sys.argv[3], 16))
    Y = ECPoint(int(sys.argv[4], 16), int(sys.argv[5], 16))

    with open(filename, 'r') as file:
        message = file.read()

    random_number = generate_random_number()
    shared_key = calculate_shared_key(G, random_number)
    hash_value = calculate_hash(str(shared_key.x) + str(shared_key.y))
    ciphertext = encrypt(message, hash_value, os.urandom(16))

    with open('ciphertext.aes', 'wb') as file:
        file.write(ciphertext)

    print("--- BEGIN EPHEMERAL KEY ---")
    print("G.x = " + hex(G.x))
    print("G.y = " + hex(G.y))
    print("Y.x = " + hex(Y.x))
    print("Y.y = " + hex(Y.y))

if __name__ == "__main__":
    main()
