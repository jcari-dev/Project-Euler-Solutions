import math

def isPrime(num):
    if num < 2: return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
            

def give_me_prime_n(nth):

    prime_list = []
    n = 0
    
    while len(prime_list) <= nth:
        if isPrime(n):
            prime_list.append(n)
        n += 1  
            
    print(prime_list[-1])

give_me_prime_n(10000) #104743
