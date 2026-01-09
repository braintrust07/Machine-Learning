def transpose_matrix(input_matrix):
    rows = len(input_matrix)
    cols = len(input_matrix[0])

    transpose = [[0 for _ in range(rows)] for _ in range(cols)] # initialize transpose matrix with swapped dimensions

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = input_matrix[i][j]  #transpose of matrix

    return transpose

def main():
    matrix = eval(input("Enter matrix (e.g. [[1,2],[3,4]]): "))

    transposed_matrix = transpose_matrix(matrix)

    print("Transpose of the matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()
