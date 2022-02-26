import numpy as np

a, b = 500, 500

for a_number in range(1, a):
    for b_number in range(1, b):
        difference = a_number + b_number
        c = 1000 - difference
        if np.square(a_number) + np.square(b_number) == np.square(
                c) and a_number < b_number < c:
            print(a_number, b_number, c,
                  a_number * b_number * c)  # (200, 375, 425, 31875000)
