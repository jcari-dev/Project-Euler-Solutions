import re
import math


grid = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

print(grid)

clean_grid = re.sub(r'[^\d]', '', grid)

# print(clean_grid)

clean_grid_list = re.findall('..', clean_grid)

final_grid = []
    
for number_string in range(0, len(clean_grid_list), 20):
    sub_grid = clean_grid_list[number_string:number_string + 20]
    int_sub_grid = [int(i) for i in sub_grid]
    final_grid.append(int_sub_grid)
    
# print(final_grid)
dim = len(final_grid) - 1
right_largest_prod = 0
down_largest_prod = 0
diagonal_largest_prod_right = 0
diagonal_largest_prod_left = 0

prod_list = []
diagonal_right = []
diagonal_left = []

for index_one,number_pair_one in enumerate(final_grid):
    right = []
    # print(final_grid[index_one:index_one+3])
    
    right = final_grid[index_one][index_one:index_one+4]
    # print(right)
    if len(right) == 4:
        
        right_sum = math.prod(right)
        if right_sum > right_largest_prod:
            right_largest_prod = right_sum
    
    for index_two,number_pair_two in enumerate(final_grid):
        down = []
        down = final_grid[index_one][index_two:index_two+4]
        if len(down) == 4:
            
            down_sum = math.prod(down)
            
            if down_sum > down_largest_prod:
                down_largest_prod = down_sum
            
        if index_one == index_two: # diagonal
            diagonal_right = final_grid[index_one:index_one+4][index_two:index_two+4]
            if len(diagonal_right) == 4:
                diagonal_sum_right = math.prod(diagonal_right)
                if diagonal_sum_right > diagonal_largest_prod_right:
                    diagonal_largest_prod_right = diagonal_sum_right
                diagonal_right = []
                
        if index_two == dim - index_one:
            diagonal_left = final_grid[index_one:index_one+4][index_two:index_two+4]
            if len(diagonal_left) == 4:
                diagonal_sum_left = math.prod(diagonal_left)
                if diagonal_sum_left > diagonal_largest_prod_left:
                    diagonal_largest_prod_left = diagonal_sum_left
                print(diagonal_left)
                diagonal_left = []


print(diagonal_largest_prod_right, right_largest_prod, down_largest_prod, diagonal_largest_prod_left)

prod_list = prod_list.sort()

print(prod_list)
print('hi')

    

