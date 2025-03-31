# Intuition : in rotate = vertical mirror operation + top-right&bottom-left mirror operation
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    dim = len(matrix)
    for i in range(dim):
        for j in range(dim // 2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][dim - 1 - j]
            matrix[i][dim - 1 - j] = tmp

    for i in range(dim):
        for j in range(dim - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[dim - 1 - j][dim - i - 1]
            matrix[dim - 1 - j][dim - i - 1] = tmp

    print(matrix)


m =[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(m)
# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
