# required import run pip install cryptography if needed
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

#Generate a cipher based on the generated key
cipher = Fernet(key)

# EXAMPLE OF AES (SYMMETRIC) ENCRYPTION
# Takes user input and encrypts using Fernet encryption
# Which is based on AES 128-bit algorithm
# Decodes using built in functions (note that the decode("utf-8") calls just convert it to String for easy concatenation)
while True:
    #While True statement causes this to loop until user aborts 
    message = input("Enter your secret message or 'stop' to quit: ")
    if message.upper() != "STOP":
        encrypted = cipher.encrypt(message.encode())
        enc_bytes = encrypted.decode("utf-8")
        decrypted = cipher.decrypt(encrypted)
        dec_bytes = decrypted.decode("utf-8")
        #prints encrypted message
        print("Encrypted message: " + enc_bytes)
        #prints decrypted message (NOT just the user entered message input)
        print("Original message: " + dec_bytes)
    else:
        break