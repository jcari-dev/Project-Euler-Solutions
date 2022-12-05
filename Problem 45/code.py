from math import sqrt


def triangularNumber(number):
    return number*(number+1)/2


def pentagonalNumber(number):
    return number*(3 * number-1)/2


def hexagonalNumber(number):
    return number*(2*number-1)


for t in range(285, 5000):
    t_number = triangularNumber(t)
    for p in range(165, 5000):
        p_number = pentagonalNumber(p)
        for h in range(143, 5000):
            h_number = hexagonalNumber(h)
            if p_number == h_number and h_number == p_number:
                if p_number > 40755:
                    print({
                        'p_number': p_number,
                        'p': p,
                        't': t,
                        'h': h
                    })

print(t_number, p_number, h_number)
