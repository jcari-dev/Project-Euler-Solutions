def find_circle_sum(n):
    top_right = n**2
    top_left = n**2 - 1 * (n-1)
    bottom_left = n**2 - 2 * (n-1)
    bottom_right = n**2 - 3 * (n-1)
    # print(top_right, "top_right")
    # print(top_left, "top_left")
    # print(bottom_right, "bottom_right")
    # print(bottom_left, "bottom_left")
    return top_right + top_left + bottom_right + bottom_left


# print(find_circle_sum(5)) # worked

result = 1

for i in range(2, 1002):
    if i % 2 == 0:
        continue
    result += find_circle_sum(i)

print(result) # 669171001
