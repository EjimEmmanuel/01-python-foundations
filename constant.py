positional_winning_lines = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7] ]

indexed_winning_lines = []

for line in positional_winning_lines:
    temp = []
    for x in line:
        x -= 1
        temp.append(x)
    indexed_winning_lines.append(temp)


winning_lines = indexed_winning_lines


connections = {
    0: [1, 3, 4],
    1: [0, 2, 4],
    2: [1, 4, 5],
    3: [0, 4, 6],
    4: [0, 1, 2, 3, 5, 6, 7, 8],
    5: [2, 4, 8],
    6: [3, 4, 7],
    7: [4, 6, 8],
    8: [4, 5, 7],
}