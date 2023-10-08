n = int(input("Size of matrix: "))

matrix = []

for i in range(n):
    line = input()
    matrix.append(list(line))

nr_squares = int((n+1)/2)

ans = ''

for square in range(nr_squares):
    lin = square
    col = square
    # top line
    while col <= (n - square - 1):
        ans = ans + matrix[lin][col]
        col = col + 1
    col = col - 1

    # right column
    lin = lin + 1
    while lin <= (n - square - 1):
        ans = ans + matrix[lin][col]
        lin = lin + 1
    lin = lin - 1

    # bottom line
    col = col - 1
    while col >= square:
        ans = ans + matrix[lin][col]
        col = col - 1
    col = col + 1

    # left column
    lin = lin - 1
    while lin > square:
        ans = ans + matrix[lin][col]
        lin = lin - 1

print(ans)
"""
firs
n_lt
oba_
htyp
"""