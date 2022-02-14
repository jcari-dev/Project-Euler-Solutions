def factors_of(n):
    factors = set()
    div = 2
    
    while n >= 2:
        if n % div == 0:
            factors.add(div)
            
            n = n / div
        else:
            div += 1

    return factors.pop()

print(factors_of(600851475143)) #6857