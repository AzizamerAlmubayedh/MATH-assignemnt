import hashlib

def SHA60v(data):
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()  # Calculate the SHA-1 hash of the input data
    first_60_bits = sha1_hash[:15]  # Take the first 60 bits (15 nibbles)
    return first_60_bits

def find_collision():
    seen_outputs = {}  # Dictionary to store hashed outputs
    collision_found = False
    
    while not collision_found:
        data1 = input("Enter the first message: ")
        data2 = input("Enter the second message: ")
        
        hashed_data1 = SHA60v(data1)
        hashed_data2 = SHA60v(data2)
        
        if hashed_data1 == hashed_data2:
            print("Collision found!")
            print(f"Message 1: '{data1}'")
            print(f"Message 2: '{data2}'")
            print(f"Hash of Message 1: {hashed_data1}")
            print(f"Hash of Message 2: {hashed_data2}")
            collision_found = True
        else:
            print("No collision found. Trying again...")

# Example usage:
find_collision()
