from rsa_python import rsa
from cryptography.fernet import Fernet
import base64
import hashlib

# Generate key pair
keyPair = rsa.generate_key_pair(500)
e = keyPair["public"]
N = keyPair["modulus"]
d = keyPair["private"]

# ID
ID = 2210002108 * 2

# Digital signature
hash_ID = hashlib.sha256(str(ID).encode()).hexdigest()  # Hash the ID
signature = rsa.sign(hash_ID, d, N)  # Sign the hash with private key

# Verify signature
verified = rsa.verify(hash_ID, signature, e, N)

if verified:
    print("Signature verified.")
else:
    print("Signature not verified.")

# Encrypt and decrypt
encrypted_ID = rsa.encrypt(str(ID), e, N)
decrypted_ID = rsa.decrypt(encrypted_ID, d, N)

print("Original ID:", ID)
print("Decrypted ID:", decrypted_ID)

# Functions for file encryption/decryption

def encrypt_file(file_path, key_str, signature):
    key = key_str[:32].encode('utf-8')
    key = base64.urlsafe_b64encode(key.ljust(32, b'='))
    
    cipher_suite = Fernet(key)
    
    with open(file_path, 'rb') as file:
        file_data = file.read()
        
    encrypted_data = cipher_suite.encrypt(file_data + signature.encode())
    
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key_str):
    key = key_str[:32].encode('utf-8')
    key = base64.urlsafe_b64encode(key.ljust(32, b'='))
    cipher_suite = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    signature = decrypted_data[-64:].decode()
    file_data = decrypted_data[:-64]
    
    # Verify signature
    hash_data = hashlib.sha256(file_data).hexdigest()
    verified = rsa.verify(hash_data, signature, e, N)
    
    if verified:
        print("Signature verified for decrypted file.")
    else:
        print("Signature not verified for decrypted file.")
    
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(file_data)

# Encrypt a file
encrypt_file('example.txt', str(decrypted_ID), signature)

# Decrypt the file
decrypt_file('example.txt.enc', str(decrypted_ID))
