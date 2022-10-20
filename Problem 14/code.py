 def collatz_sequence(num, count):
  if num == 1:
    return num

  if num % 2 == 0:
    count += 1
    return collatz_sequence(num / 2, count )
  else:
    count += 1
    return collatz_sequence(num * 3 + 1, count )

def largest_collatz(under):
  
  current = 0
  largest = [0,0]

  for number in range(1,under):
    current = collatz_sequence(number, 0)
    if current > largest[0]:
      largest[0] = current
      largest[1] = number
  
  return largest

largest_collatz(1000000)