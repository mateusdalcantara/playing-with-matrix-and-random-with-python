from hold_my_data import generate_matrix_random
from hold_my_data import print_matrix

line = int(input("give me a number to put on the matrix line: \n"))
column = int(input("give me a number to put on the matrix column: \n"))
if line > 0 and column > 0:
    matrix = generate_matrix_random(line, column)
    print_matrix(matrix)
else:
    print("number not informed...")