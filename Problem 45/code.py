from math import sqrt


def triangularNumber(number):
    """ Returns the value of the triangular number entered. """
    return number*(number+1)/2


def is_pentagonal(number):
    """ Returns True if Number is Pentagonal. """
    result = (sqrt(24*number+1)+1)/6
    return result.is_integer()


def is_hexagonal(number):
    """ Returns True if Number is Hexagonal. """
    result = (sqrt(1+8*number)+1)/4
    return result.is_integer()


t = 285
flag = False
while flag is False:
    t_number = triangularNumber(t)
    if is_pentagonal(t_number) and is_hexagonal(t_number) and t_number > 40755:
        flag = True
    t += 1

print(t_number)  # 1533776805.0
