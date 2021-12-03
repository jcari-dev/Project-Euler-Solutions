def get_me_the_sum(num, exponent):
  
  value = pow(num, exponent)

  arr_of_num = [int(x) for x in str(value)]

  sum_of_arr = sum(arr_of_num)

  return sum_of_arr



print(get_me_the_sum(2, 1000))
