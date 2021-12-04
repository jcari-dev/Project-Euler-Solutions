import math

factorial = math.factorial(100)

print(factorial)

factorial_string = [int(x) for x in str(factorial)]

print(factorial_string)

print(sum(factorial_string))

# Answer 648
