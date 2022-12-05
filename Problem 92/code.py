def sumDigits(number):
    """ Returns True if the squared sum of the digits in the squared chain of the provided number ends 
    in 89."""
    chainSum = 0

    for digit in str(number):
        digit = int(digit)
        chainSum = chainSum + digit * digit

    if chainSum == 89:
        return True
    elif chainSum == 1:
        return False

    return sumDigits(chainSum)


counter = 0

for number in range(1, 10_000_000):
    if sumDigits(number):
        counter = counter + 1

print(counter)  # 8581146
