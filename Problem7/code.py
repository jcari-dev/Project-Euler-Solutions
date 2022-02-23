import math

def isPrime(num):
    if num % 2 == 0:
        return False
    if num > 1:
        
        num_sqrt = int(math.ceil(math.sqrt(num)))
        
        for i in range(2, num_sqrt):
            if (num % i) == 0:
                response = False
                break
        else:
            response = True
        return response
            

def give_me_prime_n(nth):

    prime_list = []
    n = 0
    
    while len(prime_list) <= nth:
        if isPrime(n):
            prime_list.append(n)
        n += 1  
            
    print(prime_list[-1])

give_me_prime_n(10001) #104743
