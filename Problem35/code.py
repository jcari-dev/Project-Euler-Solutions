import math
from numpy import roll
d = []
for num in range(3,1000000,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
      d.append(num)
print(d)
for val in d:
  count = 0
  val_listed = [int(x) for x in str(val)]
  print(val_listed)
  for index, integer in enumerate(range(len(val_listed))): 
    rotation = roll(val_listed, index)
    rotation = int("".join(map(str, rotation)))
    # print(rotation)
    if rotation in d:
        count +=1
print(count)
