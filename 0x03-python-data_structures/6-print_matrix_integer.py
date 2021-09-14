#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{}{}'.format(matrix[i][j],'' if matrix[i][j] == matrix[i][-1] else ' '), end="")
        
            print('')
