import math

def check_prime(n):
    result = True
    
    for x in range(2, int(math.ceil(math.sqrt(n+1)))):
        if n % x == 0:
            result = False
            break
        
    return result

def find_prime_sum(num):
    list_of_primes = []
    
    for y in range(2, num):
        if check_prime(y):
            list_of_primes.append(y)
    return sum(list_of_primes)

print(find_prime_sum(2000000))