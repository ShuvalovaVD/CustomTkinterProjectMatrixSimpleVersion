def convert_matrix_input_to_matrix(rows, columns, matrix_input):
    # matrix_input - строка, потому что все данные, которые вводятся из полей виджетов имеют тип str
    # например, была введена матрица:  1 2
    #                                  3 4
    # тогда matrix_input будет равняться "1 2\n3 4\n", нужно преобразовать это в матрицу, т. е. двумерный список
    lst = matrix_input.split()  # разбивает строку в одномерный список, из которого сформируем двумерный
    matrix = []
    for i in range(rows):  # сначала заполняем нулями
        tmp = [0] * columns
        matrix.append(tmp)
    index = 0
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(lst[index])
            index += 1
    return matrix


def convert_matrix_to_matrix_output(rows, columns, matrix):
    s_output = ""
    for i in range(rows):
        for j in range(columns):
            s_output += str(matrix[i][j])
            s_output += " "
        s_output += "\n"
    return s_output


def multiply_matrix_by_number(rows_input, columns_input, matrix_input, number_input):  # умножает матрицу на число
    # данные в типе str, потому что все данные, которые вводятся из полей виджетов имеют тип str
    number = int(number_input)
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(rows, columns, matrix_input)
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] *= number
    # если возвратим вложенный список (matrix), то он будет неправильно отображён в поле виджета, надо возвращать str
    # если была матрица:  1 2
    #                     3 4
    # тогда надо вернуть строку "1 2\n3 4\n"
    matrix_output = convert_matrix_to_matrix_output(rows, columns, matrix)
    return matrix_output  # а вот вставлять в виджеты можно данные любых типов, необязательно str


def transpone_matrix(rows_input, columns_input, matrix_input):  # транспонирует матрицу
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(rows, columns, matrix_input)
    new_rows, new_columns = columns, rows  # размеры транспонированной матрицы меняются
    # изначально заполним новую (транспонированную) матрицу нулями
    new_matrix = []
    for i in range(new_rows):
        tmp = [0] * new_columns
        new_matrix.append(tmp)
    # теперь перезаписываем новую матрицу
    for j in range(columns):
        for i in range(rows):
            new_matrix[j][i] = matrix[i][j]
        matrix_output = convert_matrix_to_matrix_output(new_rows, new_columns, new_matrix)
    return matrix_output


def check_symmetry_of_matrix(rows_input, columns_input, matrix_input):  # проверяет матрицу на симметричность
    rows = int(rows_input)
    columns = int(columns_input)
    matrix = convert_matrix_input_to_matrix(rows, columns, matrix_input)
    # как только находит что-то несимметричное, возвращает False, иначе в самом конце если ничего не нашло - True
    if rows != columns:
        return False
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def add_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # складывает две матрицы
    rows_1 = int(rows_1_input)
    columns_1 = int(columns_1_input)
    matrix_1 = convert_matrix_input_to_matrix(rows_1, columns_1, matrix_1_input)
    rows_2 = int(rows_2_input)
    columns_2 = int(columns_2_input)
    matrix_2 = convert_matrix_input_to_matrix(rows_2, columns_2, matrix_2_input)
    # результат будет складываться в матрицу matrix1
    rows, columns = rows_1, columns_1  # предположим, что сложение матриц определено, то есть размеры одинаковые
    for i in range(rows):
        for j in range(columns):
            matrix_1[i][j] += matrix_2[i][j]
    matrix_output = convert_matrix_to_matrix_output(rows, columns, matrix_1)
    return matrix_output


def subtract_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # вычитает из первой матрицы вторую
    rows_1 = int(rows_1_input)
    columns_1 = int(columns_1_input)
    matrix_1 = convert_matrix_input_to_matrix(rows_1, columns_1, matrix_1_input)
    rows_2 = int(rows_2_input)
    columns_2 = int(columns_2_input)
    matrix_2 = convert_matrix_input_to_matrix(rows_2, columns_2, matrix_2_input)
    # результат будет сохраняться в матрицу matrix1
    rows, columns = rows_1, columns_1  # предположим, что сложение матриц определено, то есть размеры одинаковые
    for i in range(rows):
        for j in range(columns):
            matrix_1[i][j] -= matrix_2[i][j]
    matrix_output = convert_matrix_to_matrix_output(rows, columns, matrix_1)
    return matrix_output


def multiply_two_matrix(rows_1_input, columns_1_input, matrix_1_input, rows_2_input, columns_2_input, matrix_2_input):
    # умножает две матрицы
    rows_1 = int(rows_1_input)
    columns_1 = int(columns_1_input)
    matrix_1 = convert_matrix_input_to_matrix(rows_1, columns_1, matrix_1_input)
    rows_2 = int(rows_2_input)
    columns_2 = int(columns_2_input)
    matrix_2 = convert_matrix_input_to_matrix(rows_2, columns_2, matrix_2_input)
    # умножение двух матриц определено, если кол-во столбцов 2-ой = кол-ву строк 1-ой, предположим, это так
    # размер результирующей матрицы: кол-во строк 1-ой и кол-во столбцов 2-ой
    rows, columns = rows_1, columns_2
    # изначально заполним результирующую матрицу нулями
    matrix = []
    for i in range(rows):
        tmp = [0] * columns
        matrix.append(tmp)
    # при умножении двух матрицы строки первой покоординатно умножаются на столбцы второй
    for i in range(rows):
        for j in range(columns):
            # ячейка [i][j] результирующей матрицы - это i-ая строка 1-ой, умноженная покоординатно на j-ый столбец 2-ой
            for k in range(columns_1):  # или rows2, неважно, они равны, если умножение матриц определено
                matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]  # постепенно покоординатно умножаем
    matrix_output = convert_matrix_to_matrix_output(rows, columns, matrix)
    return matrix_output
