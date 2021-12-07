numbers = []

for i in range(2,101):
    for j in range(2,101):
        numbers.append(j**i)

no_dupes = []

[no_dupes.append(x) for x in numbers if x not in no_dupes]

print(len(sorted(no_dupes)))

# Answer 9183