import math
from numpy import roll

l = []
for num in range(3, 1000001, 2):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        l.append(num)

count = 1

for val in l:
    val_listed = [int(x) for x in str(val)]
    full_rotation = len(val_listed)
    for index, integer in enumerate(range(len(val_listed))):
        rotation = roll(val_listed, index)
        rotation = int("".join(map(str, rotation)))

        if rotation in l:
            full_rotation -= 1
            if full_rotation == 0:
                count += 1

        else:
            continue
print(count)
#55
