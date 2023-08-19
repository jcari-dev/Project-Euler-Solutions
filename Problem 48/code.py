accumulator = 0

for i in range(1, 1001):
    accumulator = accumulator + pow(i, i)

answer = str(accumulator)[-10:]  # 9110846700