from __future__ import print_function
import SHA60v

def collision_match(msg1, msg2):
  

    # Calculate the hashes of the two messages.
    hash1 = SHA60v(msg1)
    hash2 = SHA60v(msg2)

    # If the two hashes are equal, then we have found a collision.
    if hash1 == hash2:
        return msg1, msg2

    # Otherwise, we need to find two messages that have the same first 60 bits.
    # We can do this by brute force.
    for i in range(0x110000):  # Valid range for Unicode code points
        try:
            msg1_new = msg1 + chr(i)
            msg2_new = msg2 + chr(i)

            # Calculate the hashes of the two new messages.
            hash1_new = SHA60v(msg1_new)
            hash2_new = SHA60v(msg2_new)

            # If the two new hashes are equal, then we have found a collision.
            if hash1_new == hash2_new:
                
                return msg1_new, msg2_new
            
        except ValueError:
            
            continue

    # If we reach this point, then we have not found a collision.
    
    return None


if __name__ == "__main__":
    # Find a collision for the messages "CYS406" and "CYS406A".
    msg1 = "CYS406"
    msg2 = "CYS406b"

    collision = collision_match(msg1, msg2)

    # If we found a collision, then print it out.
    if collision is not None:
        print("Collision found:")
        print("Message 1:", collision[0])
        print("Message 2:", collision[1])
    else:
        print("No collision found.")