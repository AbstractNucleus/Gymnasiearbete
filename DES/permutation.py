from tables import *

def permutate(matrix, table, output = ""):
    for i in range(len(table)):
        output += str(matrix[table[i]])
    return output
