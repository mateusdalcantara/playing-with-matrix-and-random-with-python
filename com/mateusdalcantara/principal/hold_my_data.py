def generate_matrix_random(line, column):
    import random
    while True:
        matrix = []
        for i in range(line):
            LINE = []
            for j in range (column):
                num = random.randint(1, 10)
                LINE.append(num)
            matrix.append(LINE)
        break
    return matrix

def print_matrix(matrix):
    line = len(matrix)
    column = len(matrix[0])
    for i in range(line):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print("")