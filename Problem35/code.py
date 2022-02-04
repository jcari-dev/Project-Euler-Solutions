import math
from numpy import roll

d = []
for num in range(3, 1000001, 2):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        d.append(num)

count = 1

for val in d:
    val_listed = [int(x) for x in str(val)]
    full_rotation = len(val_listed)
    for index, integer in enumerate(range(len(val_listed))):
        rotation = roll(val_listed, index)
        rotation = int("".join(map(str, rotation)))

        if rotation in d:
            full_rotation -= 1
            if full_rotation == 0:
                count += 1

        else:
            continue
print(count)
#55
