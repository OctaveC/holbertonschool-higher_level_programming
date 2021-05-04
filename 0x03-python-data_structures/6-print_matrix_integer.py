def print_matrix_integer(matrix=[[]]):
    for columns in matrix:
        padding = ""
        for ite in columns:
            print("{}{}".format(padding, ite), end='')
            padding = " "
        print("")
