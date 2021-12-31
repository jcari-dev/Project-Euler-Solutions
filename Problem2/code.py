import functools

@functools.cache
def fib(n):
    if n <= 2:
        return 1
    else: 
        return fib(n - 1) + fib(n-2)
        
a = 2

evenFibs = []

while(fib(a) < 4000000):
    if fib(a) % 2 == 0:
        evenFibs.append(fib(a))
    a+=1

print(sum(evenFibs))
