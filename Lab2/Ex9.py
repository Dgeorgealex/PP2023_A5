def see_not(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_height = [0] * m
    pos_list = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] <= max_height[j]:
                pos_list.append((i, j))
            else:
                max_height[j] = matrix[i][j]

    return pos_list


if __name__ == "__main__":
    print(see_not([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))

