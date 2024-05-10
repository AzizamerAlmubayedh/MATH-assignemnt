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

    
    def sign(message, priv):
     # Hash the message using SHA-256
     hash = hashlib.sha256()
     hash.update(message.encode("utf-8"))
     hashed_message = hash.hexdigest()
     # Encrypt the hashed message with the private key
     signature = rsa.encrypt(hashed_message, priv, N)
     return signature

    def verify(message, signature, public_key):
        
        decrypted_signature = rsa.decrypt(signature, public_key, N)
        # Hash the message
        hash = hashlib.sha256()
        hash.update(message.encode("utf-8"))
        hashed_message = hash.hexdigest()
        # Compare the decrypted signature with the hashed message
        return decrypted_signature == hashed_message
    
    
    
    
    print(f"(Alice): \"Bob, take (N, e), p, q: ({N}, {pub}), {p}, {q}\"")
    print("\t\t\t\t\tAlice --------------------------------------------(N, e, p, q)--------------------------------------------> Bob")

    # Bob signs a message (M)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Bob): \"Thanks Alice, just wait and I will send a message.")
    print("I hope no one but you could read it. We live in a dangerous world.\"")
    print("================================================================================================================================")

    M = "This is a secret message from Bob to Alice."
    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob's message is: {M}")
    print("================================================================================================================================")

    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob is signing message M using his private key")
    print("================================================================================================================================")

    # Hashing the message
    signature = sign(M, priv)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob has created the digital signature")
    print("================================================================================================================================")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Bob): \"Alice, here's my signed message. Did you get it?\"")

    print("\t\t\t\t\tAlice <--------------------------------------------(M, Signature)-------------------------------------------- Bob")

    print("(Alice): \"Wait a sec. There we go. Thanks Bob, I have got your signed message.\"")
    print("================================================================================================================================")

    # Alice verifies the signature
    is_verified = verify(M, signature, pub)
    print("Alice is now verifying the signature using Bob's public key")
    print("================================================================================================================================")

    if is_verified:
        print("(Alice): \"The signature is verified. I trust that it's from Bob.\"")
    else:
        print("(Alice): \"The signature is not verified. I can't trust this message.\"")
    print("================================================================================================================================")

if __name__ == "__main__":
    main()
