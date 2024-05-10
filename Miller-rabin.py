#Abdulaziz Amer Almubayedh
#Date: 14/Nov/2023
#Time taken : 3.5 hours ;(
    
import random


def is_N_prime(N):
   
    if (N % 2 == 0) or (N < 2) :          # if N is even or less than 2, then it is not a prime number
        return False
                             # We that in Miller-Rabin that ---> N - 1 =   2^k * q
                             # So far the odd number is unknown
    K, q = 0, N -1            # K represents the number of times the number is divided by 2 
    
    while q % 2 == 0:
        
        K += 1
        q //= 2
    

    #============================Now we have K, q=============================================
   
    #================ Since we were asked to test 5 times for each number, then let's do this doctor================================#
    
    for i in range(5):          # iterate 5 times
        a = random.randint(2, N-1)     #each time we choose a random base such that it is greater than 1 and less than N
        result = pow(a, q, N)     # first test; we compute the random base with the q (odd) number as we found earlier modules N

        if result == 1 or result == N - 1: # If we encountered a 1 or a -1 (N-1) as a result 
            continue                        # Then there is no need to tire our selves and go to the next base                                
        
        for k in range(K - 1):          # now let us iterate over the base k times 
            
            result = pow(result, 2, N)          # as we have studied before in the binary exponentiation, we can compute the next result by using the previous on to the power of 2
            if result == N-1:                   # if we got the result as minus 1
                break
        else:
            return a, False   # now we could conclude that the current base is a witness (a) and therefore the number is composite. So it is not a prime
    return None, True # elsewhere, the number in fact is a prime. So it has no witnesses and we will return nothing here 
    
def TestingNumbers(N):
    
    witness, finalResult = is_N_prime(N)
    if finalResult:    # if the function return true, it will return the no witnesses hence it is a prime number
        print(f"The number {N} is a prime or a Carmichael number so far")
    else :                     # if the function return False (not prime), it will return a witness 
        print(F"The number {N} is composite and the witness for our crime is ---> {witness}")


TestingNumbers(531)
TestingNumbers(313)
TestingNumbers(523)
    

        
        
