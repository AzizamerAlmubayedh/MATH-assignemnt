
import hashlib
from rsa_python import rsa




def sign(message, private_key):
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = rsa.encrypt(hashed_message, private_key["d"], private_key["modulus"])
    return signature

def verify(message, signature, public_key):
    hashed_message = hashlib.sha256(message.encode()).digest()
    decrypted_signature = rsa.decrypt(signature, public_key["public"], public_key["modulus"])
    return hashed_message == decrypted_signature