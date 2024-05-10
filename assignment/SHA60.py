import hashlib
import random
import string

def SHA6v(data):
    sha1_hash = hashlib.sha1(str(data).encode()).hexdigest()  # Calculate the SHA-1 hash of the input data
    first_15_nibbles = sha1_hash[:15]  # Take the first 15 nibbles (60 bits)
    return first_15_nibbles

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def find_collision():
    seen_outputs = {}  # Initialize an empty dictionary to store hashed outputs and corresponding inputs
    num_hashes = 0  # Counter to keep track of the number of hashes calculated
    
    while True:
        # Randomly choose between generating a random number or a random string
        if random.choice([True, False]):
            data = str(random.getrandbits(32))  # Generate a random number
        else:
            data = generate_random_string(10)  # Generate a random string of length between 1 and 10
        
        hashed_data = SHA6v(data)
        num_hashes += 1
        
        if hashed_data in seen_outputs:
            print(f"Collision found after {num_hashes} hashes!")
            print(f"Collision inputs: '{data}' and '{seen_outputs[hashed_data]}'")
            print(f"Collision hash: {hashed_data}")
            break
        
        seen_outputs[hashed_data] = data

# Example usage:
find_collision()
