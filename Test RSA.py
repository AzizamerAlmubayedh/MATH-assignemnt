# Abdulaziz Amer 
# ID : 2210002108
# Date / time taken : (15/Nov/2023) almost 4 Hours
# I feel proud of this ;)




from rsa_python import rsa
from cryptography.fernet import Fernet
import base64



"""
    This beloved function generates a pair of keys of size  500 as you have requested
    Also, returns a dictionary of  (P, Q , Phi, private decryptedK, public decryptedK, and of course N)
"""
# 1 - Alice wants to generate a N by providing  2  500-bit prime numbers 

keyPair = rsa.generate_key_pair(500) # now, We have generated a dictionary that contains p, q , phi, e , d and of course N and the time it took to generate them

e = keyPair["public"] # The functions defines the "e" as "public". So, just to make it easier to be  read , I have assigned it to (e)
N = keyPair["modulus"] # again the functions defines the "N" as "modulus". So, just to make it easier to be read ,I have assigned it to (N)

print(f"(Alice) : \"Bob, take(N,e)\"")
print("\n\t\t\t\t\tAlice --------------------------------------------(N,e)--------------------------------------------> Bob")



#for decryptedK in keyPair.keys():  #hence it returns a dictionary, we want to iterate over the dictionary and print the previously mentioned elements respectively
    
    #print(f"{decryptedK} is {keyPair[decryptedK]}")
    
    
    
# 2- bob wants to encrypt his (K) with the publickey sent by Alice (N,e)

print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Bob) : \"Thanks Alice, just wait and I will send a message. I hope no one but you could read it. We live in a dangerous world.  \"")
print("\n================================================================================================================================\n")

K = 22100021082210002108 # in this section, I chose to make the K my ID*2 .hehe :)
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob's 20-bit decryptedK is {K}")
print("\n================================================================================================================================\n")


print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob is encrypting K by using the following: ({K}) ^ e mod N ")
print("\n================================================================================================================================\n")

encryptK = rsa.encrypt(str(K), e,N) # now Bob has encrypted his K with the public key
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tBob has done the encryption ")
print("\n================================================================================================================================\n")



# 3- Alice takes the encrypted K and do the decrypting process hence she and only she has the inverse of e
print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Bob) : \"Alice  here, take my message. Did you get it ?\"................................")

print("\n\t\t\t\t\tAlice <--------------------------------------------(C)-------------------------------------------- Bob")

d = keyPair["private"] #again the functions defines the "d" as "private". So, just to make it easier to be read ,I have assigned it to (d)
print("\n(Alice): \"Wait a sec. There we go. Thanks Bob I have got your message :)\"")
print("\n================================================================================================================================\n")

decryptedK = rsa.decrypt(encryptK, d,N) 
print(f"\nAlice is now decrypting the value with the following:   C^{d} mod N")
print("\n================================================================================================================================\n")

print(f"\n(Alice) : \"Horaaaaaaaaaaaaaaaaaaaaaaaaaaaay......................:\"\n{decryptedK}")
print("\n================================================================================================================================\n")







def encrypt_file(file_path, key_str): # this one however, takes any file and reads its data then it encrypts that data then write the encrypted data to the same file 
                                         # hence ('wb') overwrite the contend of a file, the previously encrypted data are written here. As a result, the  file's contents are has been encrypted
    key = key_str[:32].encode('utf-8')
    key = base64.urlsafe_b64encode(key.ljust(32, b'='))
    
    cipher_suite = Fernet(key)
    
    with open(file_path, 'rb') as file:
        
        file_data = file.read()
        
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
        
        

        
        

def decrypt_file(encrypted_file_path, key_str): # to be efficient with you, this function basicly takes the a file and decrypts its data (The opposite of the previous one )
    
    key = key_str[:32].encode('utf-8')
    key = base64.urlsafe_b64encode(key.ljust(32, b'='))
    cipher_suite = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as encrypted_file:
        
        encrypted_data = encrypted_file.read()
        
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        
        decrypted_file.write(decrypted_data)
        
        



# Encrypt a file
encrypt_file(r'C:\Users\Aziz\PycharmProjects\Programing-for-Cyber\Programing-for-Cyber\Math assignment\example.txt', decryptedK)  # Now take any file that you have and place it here doctor, it will use the key "K" to encrypt the file contents 

# Decrypt the file
decrypt_file(r'C:\Users\Aziz\PycharmProjects\Programing-for-Cyber\Programing-for-Cyber\Math assignment\example.txt.enc', decryptedK) # here, plce the file you just placed. It will use the key "K" to decrypt the file contents


