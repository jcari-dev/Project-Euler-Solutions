squares = [i**2 for i in range(1,101)]

squared = [i for i in range(1,101)]

sum_of_squares = sum(squares)

squared_sum = sum(squared)**2

difference_between_them = squared_sum-sum_of_squares

print(difference_between_them)

