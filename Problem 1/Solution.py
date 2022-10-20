
multiples_of_3_and_5 = []
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        multiples_of_3_and_5.append(number)
        
multiples_of_3_and_5 = sum(multiples_of_3_and_5)
print(multiples_of_3_and_5)