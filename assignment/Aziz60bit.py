import hashlib

def SHA60v(msg):
    """Returns the first 60 bits of the SHA-1 hash of the given message."""
    # Calculate the SHA-1 hash of the message.
    hash_object = hashlib.sha1(msg.encode())
    hash_hex = hash_object.hexdigest()

    # Return the first 60 bits of the hash.
    return hash_hex[:15]

# Example usage
message = "CYS406"
result = SHA60v(message)
print(result)