#Craeted by Abdulaziz Amer Almubayedh 
#ID : 2210002108
#Date : 2023/Nov/11



def gcd(a, b):                          #* this method finds the GCD of 2 give nelements
    
    
    a, b = max(a, b), min(a, b)         # To ensure that (a) is being the largest of the two
    

    while b > 0:                        # to make sure that if (b) [the smallest of the two] reached 0, we get the final result which is [a]
        
        a, b = b, a % b
        
    return a                                # the final result 

def hasInverse(a, b):
    
    result = gcd(a, b)                  #* this method checks if a number has an inverse of b
    
    if result == 1:
        
        return True
    
    else:
        
        raise ValueError(f"Inverse does not exist because the gcd between {a} and {b} is  { gcd(a,b)}")
        

def extended_gcd(a, b):                 #* this method calculates the gcd in an extended manner
    
    if a == 0:
        
        return b, 0, 1
    
    else:
        
        gcd, x, y = extended_gcd(b % a, a)
        
        return gcd, y - (b // a) * x, x
    

def FindInverse(a, b):                #* this method findsthe inverse, if it exists
    
    if hasInverse(a, b):                # we check if (a) could have an inverse?
        
        _, x, _ = extended_gcd(a, b)    # if yes, calculate the Euclidean algorithm to find the inverse
        return x % b                    # return the inverse

#------------------------------------------------------ Taking input from the user------------------------------------------------------#
try:
    
    A = int(input("Enter the value of a: "))
    B = int(input("Enter the value of b: "))            # To make sure that the given values are integers
    
except ValueError:
    
    print("Please enter valid integers.")


#------------------------------------------------------ Calculating and printing the inverse------------------------------------------------------#
try:
    
    
    if hasInverse(A, B):
        
        result = FindInverse(A, B)
        
        print(f"The multiplicative inverse of {A} modulo {B} is: {result}")                         # just to handle if any problem occures
    else:
        print(f"{A} does not have an inverse modulo {B}")
    
except Exception as e:
    
    print("Exception---------->", e)
    
