def check_palindrome(num):

    num = str(num)

    num_list = list(num)

    num_length = len(num_list)

    middle_index = num_length // 2

    first_half = num_list[:middle_index]

    reversed_second_half = list(reversed(num_list[middle_index:]))

    if ''.join(first_half) == ''.join(reversed_second_half):
        return True
    else:
        return False


# check_palindrome(4114)


def check_palindrome_product_of(nth):  #digits

    digits = 10**nth - 1

    list_of_numbers = list(range(1, digits + 1))

    largest_palindrome_product = 0

    for number in list_of_numbers:
        for digit in range(1, digits + 1):
            product = number * digit
            if check_palindrome(
                    product) and product > largest_palindrome_product:
                largest_palindrome_product = product
    print(largest_palindrome_product)


check_palindrome_product_of(3)  #906609
