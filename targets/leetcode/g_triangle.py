
# 118_Pascal's_Triangle

def g_triangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = []
    for i in range(numRows):
        result.append([0] * (i + 1))
    for i in range(numRows):
        for j in range(i + 1):
            if j == 0 or j == i:
                result[i][j] = 1
            else:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result

print(g_triangle(5))    # pragma: no cover
