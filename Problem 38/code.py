def strip_from_left(n):
    div = 1
    while n // div >= 10:
        div *= 10
    return n % div


def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def is_truncatable(n):
    if n < 10:
        return False

    left = n
    right = n

    while left > 0:
        if not is_prime(left):
            return False
        left = strip_from_left(left)

    while right > 0:
        if not is_prime(right):
            return False
        right //= 10

    return True


truncatables = []
n = 11

while len(truncatables) < 11:
    if is_truncatable(n):
        truncatables.append(n)
    n += 1

print(truncatables)
print(sum(truncatables))  #748317