

def sumDigits(number, seen=None):
    """ Returns the squared sum of the digits of the provided number."""
    chainSum = 0
    if seen is None:
        seen_numbers = []
    else:
        seen_numbers = seen

    for digit in str(number):
        digit = int(digit)
        chainSum = chainSum + digit * digit

    seen_numbers.append(chainSum)

    if chainSum in [89, 1]:
        if chainSum == 89:
            return seen_numbers
        elif chainSum == 1:
            return False
    return sumDigits(chainSum, seen_numbers)


ending_in_89 = []

counter = 0

for number in [85, 89, 145, 42, 20]:
    if sumDigits(number):
        if number in ending_in_89:
            print(number, 'skipped!')
            counter = counter + 1
            continue
        for value in sumDigits(number):
            if value not in ending_in_89:
                ending_in_89.append(value)
        counter = counter + 1

print(counter)
