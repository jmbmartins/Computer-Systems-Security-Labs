from Crypto import Random
import binascii
from Pratical.Lab_07.ecc import ECPoint

def main():
    # Ponto base
    G = ECPoint(int("188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012", 16), int("7192b95ffc8da78631011ed6b24cdd573f977a11e794811", 16))

    # Gere um número aleatório de 192 bits para a chave privada
    rnd = Random.new()
    private_key = int(binascii.hexlify(rnd.read(24)), 16)

    # Calcule a chave pública multiplicando o ponto base pela chave privada
    public_key = G.multiplyPointByScalar(private_key)

    print("--- BEGIN PRIVATE KEY ---")
    print(hex(private_key))

    print("--- BEGIN PUBLIC KEY ---")
    print("pk.x = " + hex(public_key.x))
    print("pk.y = " + hex(public_key.y))

    print("G.x = " + hex(G.x))
    print("G.y = " + hex(G.y))

if __name__ == "__main__":
    main()
