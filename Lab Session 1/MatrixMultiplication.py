def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:  # check if matrices are multipliable
        return None

    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]  # initialize result matrix

    for i in range(rows_a):  # do matrix multiplication
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result_matrix


def main():
    matrix_a = eval(input("Enter Matrix A (e.g. [[1,2],[3,4]]): "))
    matrix_b = eval(input("Enter Matrix B (e.g. [[5,6],[7,8]]): "))

    product = multiply_matrices(matrix_a, matrix_b)

    if product is None:
        print("Error: Matrices are not multipliable")
    else:
        print("Matrix Product:")
        for row in product:
            print(row)


if __name__ == "__main__":
    main()
