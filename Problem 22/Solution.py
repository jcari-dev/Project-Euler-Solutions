import string


def score_name(name, index):
    score_sum = 0
    index += 1
    for character in name.lower():
        alphabet_position = string.ascii_lowercase.index(character) + 1
        score_sum += alphabet_position
    return score_sum * index


with open("names.txt") as file:
    names = file.read().split('","')

clean_names = [name.replace('"', "") for name in names]

alphabetically_sorted = sorted(clean_names)

file_sum = 0

for index, name in enumerate(alphabetically_sorted):
    name_score = score_name(name, index)
    file_sum += name_score

print(file_sum)  # 871198282
