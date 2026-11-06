# Required imports, also be sure that cryptography is installed with pip install cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from getpass import getpass

# Generates a private RSA key of size 2048 bits
private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
)

# Generates a public key for the previously generated private key
public_key = private_key.public_key()

# Writes the private key to a file called 'private.pem'
with open("private.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Writes the public key to a file called 'public.pem'
with open("public.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

# Takes a user input string & converts to bits for encryption
while True:
    message = getpass("Enter your secret message or 'quit' to quit: ")
    if message.upper() != "QUIT":
        message_bytes = message.encode()

        # from the previous message variable, encrypts using the SHA256 hashing algorithm
        encrypted = public_key.encrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Prints the encrypted message (will just look like gibberish)
        print(encrypted)

        print("Decrypting message... ")

        # Decrypts the message using the private key generated at the beginning
        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Prints out the decrypted message (NOT just the original user input (though the two will be the same))
        print(decrypted)
    else:
        break