import hashlib
from rsa_python import rsa



def main():
    # Generate RSA key pair
    keyPair = rsa.generate_key_pair(256)
    p = keyPair["p"]
    q = keyPair["q"]
    pub = keyPair["public"]
    priv = keyPair["private"]
    N = keyPair["modulus"]

    
    def sign(file, priv):
     # Hash the file using SHA-256
     hash = hashlib.sha256()
     hash.update(file.encode("utf-8"))
     hashed_message = hash.hexdigest()
     # Encrypt the hashed file with the private key
     signature = rsa.encrypt(hashed_message, priv, N)
     return signature

    def verify(file, signature, public_key):
        
        decrypted_signature = rsa.decrypt(signature, public_key, N)
        # Hash the file
        hash = hashlib.sha256()
        hash.update(file.encode("utf-8"))
        hashed_message = hash.hexdigest()
        # Compare the decrypted signature with the hashed file
        return decrypted_signature == hashed_message
    
    
    
    
    M = "x"
        # Hashing the file
    signature = sign(M, priv)

    # Alice verifies the signature
    is_verified = verify(M, signature, pub)
    
    if is_verified:
        
        return True
    else:
        return False

        
    
if __name__ == "__main__":
        main()
