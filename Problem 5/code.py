number_range = range(1, 11, 1)

number_list = list(number_range)

divided = False
number = 1

while divided == False:
    new_number_list = [number % i == 0 for i in number_list]
    if not False in new_number_list:
        divided = True
        print(number)
    else:
        number += 1
