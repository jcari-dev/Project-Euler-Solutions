from num2words import num2words #pip install num2words
import re

total_words_used = 0

for number in range(1, 1001):
    clean_number = re.sub(r'[^A-Za-z]', '', num2words(number))
    total_words_used += len(clean_number)
    
print(total_words_used) #21124
