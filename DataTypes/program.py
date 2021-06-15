def return_stringList():
    return ["a","b"]

def return_2dmatrix():
    rows = 5
    cols = 3
    matrix = [[None]*cols  for _ in range(rows)]

    ch = 'a'
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = ch
            temp = ord(ch) + 1
            ch = chr(temp)

    return matrix

def return_jagged_matrix():
    jagged_matrix = []
    rows = 5
    cols = 3
    ch = 'a'

    for i in range(rows):
        tempList = []
        for j in range(cols):
            tempList.append(ch)
            temp = ord(ch) + 1
            ch = chr(temp)
        jagged_matrix.append(tempList)
    return jagged_matrix

    
if __name__ == "__main__":
    ar = return_stringList()
    print(ar)
    str = ''.join(ar)
    print(str)

    matrix = return_2dmatrix()
    print(matrix)
    matrix = return_jagged_matrix()
    print(matrix)