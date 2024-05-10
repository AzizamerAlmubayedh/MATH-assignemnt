from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Dict
import hashlib
from rsa_python import rsa

app = FastAPI()

def generate_key_pair() -> Dict[str, int]:
    key_pair = rsa.generate_key_pair(256)
    return {
        "public_key": key_pair["public"],
        "private_key": key_pair["private"],
        "modulus": key_pair["modulus"]
    }

def sign_file(file_content: bytes, private_key: int, modulus: int) -> bytes:
    # Hash the file content using SHA-256
    hash_object = hashlib.sha256()
    hash_object.update(file_content)
    hashed_message = hash_object.digest()
    # Encrypt the hashed message with the private key
    signature = rsa.encrypt(hashed_message, private_key, modulus)
    return signature

def verify_signature(file_content: bytes, signature: bytes, public_key: int, modulus: int) -> bool:
    # Decrypt the signature using the public key
    decrypted_signature = rsa.decrypt(signature, public_key, modulus)
    # Hash the file content using SHA-256
    hash_object = hashlib.sha256()
    hash_object.update(file_content)
    hashed_message = hash_object.digest()
    # Compare the decrypted signature with the hashed file content
    return decrypted_signature == hashed_message

@app.post("/generate-key-pair")
async def generate_rsa_key_pair() -> Dict[str, int]:
    return generate_key_pair()

@app.post("/sign-file")
async def sign_file_endpoint(file: UploadFile = File(...), private_key: int = None, modulus: int = None) -> bytes:
    try:
        file_content = await file.read()
        if private_key is None or modulus is None:
            raise HTTPException(status_code=400, detail="Private key and modulus must be provided.")
        signature = sign_file(file_content, private_key, modulus)
        return signature
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/verify-signature")
async def verify_signature_endpoint(file: UploadFile = File(...), signature: bytes = None, public_key: int = None, modulus: int = None) -> Dict[str, bool]:
    try:
        file_content = await file.read()
        if signature is None or public_key is None or modulus is None:
            raise HTTPException(status_code=400, detail="Signature, public key, and modulus must be provided.")
        is_verified = verify_signature(file_content, signature, public_key, modulus)
        return {"is_verified": is_verified}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
