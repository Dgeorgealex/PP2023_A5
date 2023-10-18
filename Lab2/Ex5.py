def change_matrix(matrix):
    n = len(matrix)
    ok = True
    for line in matrix:
        if len(line) != n:
            ok = False

    if not ok:
        return 'Impossible'

    for col in range(n-1):
        matrix[col+1][col] = 0

    return matrix


if __name__ == "__main__":
    print(change_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))