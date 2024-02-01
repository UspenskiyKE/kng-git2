#Домашнее задание1
def xod(matrix):
    r = int(input("Введите номер строки\n"))
    c = int(input("Введите номер столбца\n"))
    symbol = input("Введите X или O для заполнения клетки\n")
    if 1 <= r <= 3 and 1 <= c <= 3 and (symbol == "X" or symbol == "O"):
        if matrix[r - 1][c - 1] == "*":
            matrix[r - 1][c - 1] = symbol
        else:
            print("Клетка занята. Выберите другую!")
    else:
        print("Номер строки и столбца должен быть в интервале от 1 до 3 включительно. Крестик - буква X,")
        print("нолик - буква О в заглавном регистре в английской раскладке. ")


def matrix_full(matrix):
    result = True
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1):
            if matrix[i][j] == "*":
                result = False
    return result


def row_full(matrix):
    result = False
    if matrix[0][0] == matrix[0][1] == matrix[0][2] == "X" or matrix[0][0] == matrix[0][1] == matrix[0][2] == "O" or \
            matrix[1][0] == matrix[1][1] == matrix[1][2] == "X" or matrix[1][0] == matrix[1][1] == matrix[1][
        2] == "O" or matrix[2][0] == matrix[2][1] == matrix[2][2] == "X" or matrix[2][0] == matrix[2][1] == matrix[2][
        2] == "O":
        result = True

    return result


def column_full(matrix):
    result = False
    if matrix[0][0] == matrix[1][0] == matrix[2][0] == "X" or matrix[0][0] == matrix[1][0] == matrix[2][0] == "O" or \
            matrix[0][1] == matrix[1][1] == matrix[2][1] == "X" or matrix[0][1] == matrix[1][1] == matrix[2][
        1] == "O" or matrix[0][2] == matrix[1][2] == matrix[2][2] == "X" or matrix[0][2] == matrix[1][2] == matrix[2][
        2] == "O":
        result = True

    return result


def diagonal_full(matrix):
    result = False
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == "X" or matrix[0][0] == matrix[1][1] == matrix[2][2] == "O" or \
            matrix[0][2] == matrix[1][1] == matrix[2][0] == "X" or matrix[0][2] == matrix[1][1] == matrix[2][0] == "O":
        result = True
    return result


def game_over(matrix):
    result = False
    if row_full(matrix) or column_full(matrix) or diagonal_full(matrix) or matrix_full(matrix):
        result = True
        print("Игра окончена!")
    return result


def print_matrix(matrix):
    print("  1  2  3")
    print("1 ", matrix[0][0], matrix[0][1], matrix[0][2])
    print("2 ", matrix[1][0], matrix[1][1], matrix[1][2])
    print("3 ", matrix[2][0], matrix[2][1], matrix[2][2])


# Создаём пустую матрицу 3*3
rows = 3
columns = 3
M = [["*" for j in range(columns)] for i in range(rows)]

while not game_over(M):
    print_matrix(M)
    xod(M)
print_matrix(M)

