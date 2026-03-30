def find_triangle_number(n):
    return (n + 1) * n // 2

file_path = "words.txt"

words_clean = []
longest_word_length = 0
longest_word = ""

needed_triangle_numbers = []


with open(file_path, 'r') as file:
    content = file.read()
    content = content.split(",")

    for word in content:
        clean_word = word.replace('"', "")

        words_clean.append(clean_word)
        clean_word_length = len(clean_word)

        if clean_word_length > longest_word_length:
            longest_word_length = clean_word_length
            longest_word = clean_word
index = 1

while index <= 27:  # is because 26 + 1 because we have 0
    needed_triangle_numbers.append(find_triangle_number(index))

    index += 1

print(needed_triangle_numbers)


def get_letter_value(letter):
    # print(word, "this is word")

    return ord(letter) - ord('A') + 1


def get_word_value(word):
    # print(word, "????")
    value = 0
    for letter in word:
        value += get_letter_value(letter)

    return value


# print(get_word_value("ABILITY") in needed_triangle_numbers)
# 

result = 0

for word in words_clean:
    if get_word_value(word) in needed_triangle_numbers:
        result += 1

print(result) #162
