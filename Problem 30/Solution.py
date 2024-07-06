def find_fifth_power_digits():
    fifth_powers = []
    for number in range(2, 1000000):
        number_sum = sum([int(i) ** 5 for i in str(number)])
        if number_sum == number:
            fifth_powers.append(number)
    return sum(fifth_powers)


print(find_fifth_power_digits())  # 443839
