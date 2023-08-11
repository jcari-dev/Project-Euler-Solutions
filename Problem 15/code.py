import math

def determine_lattice_paths(m, n):
    # m stands for the number of rows
    # n stands for the number of columns
    
    m_factorial = math.factorial(m)
    n_factorial = math.factorial(n)
    
    number_of_routes = math.factorial(m + n) / (m_factorial * n_factorial)
    
    return number_of_routes

print(determine_lattice_paths(20, 20)) # 137846528820