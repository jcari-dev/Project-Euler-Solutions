from functools import reduce


def get_triangle_number(nth):

    factors = []
    triangle_number_terms = []
    sum_number_terms = []
    number = 1

    while len(factors) < nth:
        triangle_number_terms.append(number)
        terms_sum = reduce(lambda x,y: x+y, triangle_number_terms)
        sum_number_terms.append(terms_sum)
        factors = [n for n in range(1, terms_sum +1) if terms_sum % n == 0]
        number += 1
    
        
    
    return sum_number_terms, factors, terms_sum

print(get_triangle_number(100))
    
    