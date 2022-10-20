from functools import reduce
import math


def get_triangle_number_more_than(nth):

    factors = []
    triangle_number_terms = []
    sum_number_terms = []
    number = 1

    while not len(factors) > nth:
        triangle_number_terms.append(number)
        terms_sum = reduce(lambda x,y: x+y, triangle_number_terms)
        sum_number_terms.append(terms_sum)
        factors = [n for n in range(1, terms_sum+ 1) if terms_sum % n == 0]
        number += 1
    
        
    number_of_factors = len(factors)
    return print(f"the number {terms_sum}, has {number_of_factors} factors, which is larger than {nth}")

print(get_triangle_number_more_than(500))
    
    