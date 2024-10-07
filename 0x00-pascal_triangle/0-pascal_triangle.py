
'''
    Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
'''
def pascal_triangle(n):
    if n <=0:
        return []
    
    pascal_t = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_t[i-1][j-1] + pascal_t[i-1][j])
        row.append(1)
        pascal_t.append(row)

    return pascal_t

 