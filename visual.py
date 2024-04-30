import customtkinter as ctk  # подключаем модуль customtkinter

# функции, которые отрисовывают и стирают окна

def show_window_menu_option_choice():
    global root, start_message_lbl, choose_option_message_lbl, options_choice_combobox, choose_option_btn_done
    # задаём сетку для этого окна: 4 x 1
    rows, columns = 4, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    start_message_lbl.grid(row=0, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    choose_option_message_lbl.grid(row=1, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    options_choice_combobox.grid(row=2, column=0, ipadx=4, padx=100, pady=20, sticky="ew")
    choose_option_btn_done.grid(row=3, column=0, ipadx=4, ipady=4, padx=300, pady=20, sticky="nsew")


def clear_window_menu_option_choice():
    global root, start_message_lbl, choose_option_message_lbl, options_choice_combobox, choose_option_btn_done
    # скрываем виджеты
    start_message_lbl.grid_forget()
    choose_option_message_lbl.grid_forget()
    options_choice_combobox.grid_forget()
    choose_option_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 4, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_size_input():
    global root, matrix_size_input_message_lbl, matrix_rows_input_message_lbl, matrix_columns_input_message_lbl,\
        matrix_rows_input_entry, matrix_columns_input_entry, matrix_size_input_btn_cancel, matrix_size_input_btn_done
    # задаём сетку для этого окна: 4 x 2
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_size_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_rows_input_message_lbl.grid(row=1, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_columns_input_message_lbl.grid(row=2, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_rows_input_entry.grid(row=1, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_columns_input_entry.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_size_input_btn_cancel.grid(row=3, column=0, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")
    matrix_size_input_btn_done.grid(row=3, column=1, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")


def clear_window_matrix_size_input():
    global root, matrix_size_input_message_lbl, matrix_rows_input_message_lbl, matrix_columns_input_message_lbl, \
        matrix_rows_input_entry, matrix_columns_input_entry, matrix_size_input_btn_cancel, matrix_size_input_btn_done
    # скрываем виджеты
    matrix_size_input_message_lbl.grid_forget()
    matrix_rows_input_message_lbl.grid_forget()
    matrix_columns_input_message_lbl.grid_forget()
    matrix_rows_input_entry.grid_forget()
    matrix_columns_input_entry.grid_forget()
    matrix_size_input_btn_cancel.grid_forget()
    matrix_size_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_1_size_input():
    global root, matrix_1_size_input_message_lbl, matrix_1_rows_input_message_lbl, matrix_1_columns_input_message_lbl, \
        matrix_1_rows_input_entry, matrix_1_columns_input_entry, matrix_1_size_input_btn_cancel, \
        matrix_1_size_input_btn_done
    # задаём сетку для этого окна: 4 x 2
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_1_size_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_1_rows_input_message_lbl.grid(row=1, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_1_columns_input_message_lbl.grid(row=2, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_1_rows_input_entry.grid(row=1, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_1_columns_input_entry.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_1_size_input_btn_cancel.grid(row=3, column=0, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")
    matrix_1_size_input_btn_done.grid(row=3, column=1, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")


def clear_window_matrix_1_size_input():
    global root, matrix_1_size_input_message_lbl, matrix_1_rows_input_message_lbl, matrix_1_columns_input_message_lbl, \
        matrix_1_rows_input_entry, matrix_1_columns_input_entry, matrix_1_size_input_btn_cancel, \
        matrix_1_size_input_btn_done
    # скрываем виджеты
    matrix_1_size_input_message_lbl.grid_forget()
    matrix_1_rows_input_message_lbl.grid_forget()
    matrix_1_columns_input_message_lbl.grid_forget()
    matrix_1_rows_input_entry.grid_forget()
    matrix_1_columns_input_entry.grid_forget()
    matrix_1_size_input_btn_cancel.grid_forget()
    matrix_1_size_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_2_size_input():
    global root, matrix_2_size_input_message_lbl, matrix_2_rows_input_message_lbl, matrix_2_columns_input_message_lbl, \
        matrix_2_rows_input_entry, matrix_2_columns_input_entry, matrix_2_size_input_btn_cancel, \
        matrix_2_size_input_btn_done
    # задаём сетку для этого окна: 4 x 2
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_2_size_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_2_rows_input_message_lbl.grid(row=1, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_2_columns_input_message_lbl.grid(row=2, column=0, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_2_rows_input_entry.grid(row=1, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_2_columns_input_entry.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=6, sticky="nsew")
    matrix_2_size_input_btn_cancel.grid(row=3, column=0, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")
    matrix_2_size_input_btn_done.grid(row=3, column=1, ipadx=4, ipady=20, padx=20, pady=6, sticky="nsew")


def clear_window_matrix_2_size_input():
    global root, matrix_2_size_input_message_lbl, matrix_2_rows_input_message_lbl, matrix_2_columns_input_message_lbl, \
        matrix_2_rows_input_entry, matrix_2_columns_input_entry, matrix_2_size_input_btn_cancel, \
        matrix_2_size_input_btn_done
    # скрываем виджеты
    matrix_2_size_input_message_lbl.grid_forget()
    matrix_2_rows_input_message_lbl.grid_forget()
    matrix_2_columns_input_message_lbl.grid_forget()
    matrix_2_rows_input_entry.grid_forget()
    matrix_2_columns_input_entry.grid_forget()
    matrix_2_size_input_btn_cancel.grid_forget()
    matrix_2_size_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 4, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_input():
    global root, matrix_input_message_lbl, matrix_input_textbox, matrix_input_btn_cancel, matrix_input_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_input_textbox.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    matrix_input_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    matrix_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_matrix_input():
    global root, matrix_input_message_lbl, matrix_input_textbox, matrix_input_btn_cancel, matrix_input_btn_done
    # скрываем виджеты
    matrix_input_message_lbl.grid_forget()
    matrix_input_textbox.grid_forget()
    matrix_input_btn_cancel.grid_forget()
    matrix_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_1_input():
    global root, matrix_1_input_message_lbl, matrix_1_input_textbox, matrix_1_input_btn_cancel, matrix_1_input_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_1_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_1_input_textbox.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    matrix_1_input_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    matrix_1_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_matrix_1_input():
    global root, matrix_1_input_message_lbl, matrix_1_input_textbox, matrix_1_input_btn_cancel, matrix_1_input_btn_done
    # скрываем виджеты
    matrix_1_input_message_lbl.grid_forget()
    matrix_1_input_textbox.grid_forget()
    matrix_1_input_btn_cancel.grid_forget()
    matrix_1_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_2_input():
    global root, matrix_2_input_message_lbl, matrix_2_input_textbox, matrix_2_input_btn_cancel, matrix_2_input_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_2_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_2_input_textbox.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    matrix_2_input_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    matrix_2_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_matrix_2_input():
    global root, matrix_2_input_message_lbl, matrix_2_input_textbox, matrix_2_input_btn_cancel, matrix_2_input_btn_done
    # скрываем виджеты
    matrix_2_input_message_lbl.grid_forget()
    matrix_2_input_textbox.grid_forget()
    matrix_2_input_btn_cancel.grid_forget()
    matrix_2_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_number_input():
    global root, number_input_message_lbl, number_input_entry, number_input_btn_cancel, number_input_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    number_input_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    number_input_entry.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    number_input_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    number_input_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_number_input():
    global root, number_input_message_lbl, number_input_entry, number_input_btn_cancel, number_input_btn_done
    # скрываем виджеты
    number_input_message_lbl.grid_forget()
    number_input_entry.grid_forget()
    number_input_btn_cancel.grid_forget()
    number_input_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_result_output():
    global root, matrix_result_output_message_lbl, matrix_result_output_textbox, matrix_result_output_btn_cancel, \
        matrix_result_output_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_result_output_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_result_output_textbox.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    matrix_result_output_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    matrix_result_output_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_matrix_result_output():
    global root, matrix_result_output_message_lbl, matrix_result_output_textbox, matrix_result_output_btn_cancel, \
        matrix_result_output_btn_done
    # скрываем виджеты
    matrix_result_output_message_lbl.grid_forget()
    matrix_result_output_textbox.grid_forget()
    matrix_result_output_btn_cancel.grid_forget()
    matrix_result_output_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def show_window_matrix_check_symmetry_output():
    global root, matrix_check_symmetry_output_message_lbl, matrix_check_symmetry_output_entry, \
        matrix_check_symmetry_output_btn_cancel, matrix_check_symmetry_output_btn_done
    # задаём сетку для этого окна: 3 x 2
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)
    # располагаем виджеты в данной сетке
    matrix_check_symmetry_output_message_lbl.grid(row=0, column=0, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    matrix_check_symmetry_output_entry.grid(row=1, column=0, columnspan=2, ipadx=4, ipady=4, padx=200, pady=6, sticky="nsew")
    matrix_check_symmetry_output_btn_cancel.grid(row=2, column=0, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")
    matrix_check_symmetry_output_btn_done.grid(row=2, column=1, ipadx=4, ipady=4, padx=20, pady=20, sticky="nsew")


def clear_window_matrix_check_symmetry_output():
    global root, matrix_check_symmetry_output_message_lbl, matrix_check_symmetry_output_entry, \
        matrix_check_symmetry_output_btn_cancel, matrix_check_symmetry_output_btn_done
    # скрываем виджеты
    matrix_check_symmetry_output_message_lbl.grid_forget()
    matrix_check_symmetry_output_entry.grid_forget()
    matrix_check_symmetry_output_btn_cancel.grid_forget()
    matrix_check_symmetry_output_btn_done.grid_forget()
    # стираем сетку: задаём веса=0 по умолчанию
    rows, columns = 3, 2
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)

# функции-обработчики событий

def handle_pressing_choose_option_btn_done():
    global options_choice_combobox, flag_option
    flag_option = options_choice_combobox.get()
    clear_window_menu_option_choice()
    if flag_option in ("Умножение матрицы на число", "Транспонирование матрицы",
                       "Проверка матрицы на симметричность"):
        show_window_matrix_size_input()
    else:
        show_window_matrix_1_size_input()


def handle_pressing_matrix_size_input_btn_done():
    clear_window_matrix_size_input()
    show_window_matrix_input()


def handle_pressing_matrix_size_input_btn_cancel():
    clear_window_matrix_size_input()
    show_window_menu_option_choice()


def handle_pressing_matrix_1_size_input_btn_done():
    clear_window_matrix_1_size_input()
    show_window_matrix_1_input()


def handle_pressing_matrix_1_size_input_btn_cancel():
    clear_window_matrix_1_size_input()
    show_window_menu_option_choice()


def handle_pressing_matrix_2_size_input_btn_done():
    clear_window_matrix_2_size_input()
    show_window_matrix_2_input()


def handle_pressing_matrix_2_size_input_btn_cancel():
    clear_window_matrix_2_size_input()
    show_window_matrix_1_input()


def handle_pressing_matrix_input_btn_done():
    global flag_option
    clear_window_matrix_input()
    if flag_option == "Умножение матрицы на число":
        show_window_number_input()
    elif flag_option == "Транспонирование матрицы":
        show_window_matrix_result_output()
    else:  # flag_option == "Проверка матрицы на симметричность"
        show_window_matrix_check_symmetry_output()


def handle_pressing_matrix_input_btn_cancel():
    clear_window_matrix_input()
    show_window_matrix_size_input()


def handle_pressing_matrix_1_input_btn_done():
    clear_window_matrix_1_input()
    show_window_matrix_2_size_input()


def handle_pressing_matrix_1_input_btn_cancel():
    clear_window_matrix_1_input()
    show_window_matrix_1_size_input()


def handle_pressing_matrix_2_input_btn_done():
    clear_window_matrix_2_input()
    show_window_matrix_result_output()


def handle_pressing_matrix_2_input_btn_cancel():
    clear_window_matrix_2_input()
    show_window_matrix_2_size_input()


def handle_pressing_number_input_btn_done():
    clear_window_number_input()
    show_window_matrix_result_output()


def handle_pressing_number_input_btn_cancel():
    clear_window_number_input()
    show_window_matrix_input()


def handle_pressing_matrix_result_output_btn_done():
    clear_window_matrix_result_output()
    show_window_menu_option_choice()


def handle_pressing_matrix_result_output_btn_cancel():
    global flag_option
    clear_window_matrix_result_output()
    if flag_option == "Умножение матрицы на число":
        show_window_number_input()
    elif flag_option == "Транспонирование матрицы":
        show_window_matrix_input()
    else:  # flag_option in ("Сложение двух матриц", "Вычитание двух матриц", "Умножение двух матриц")
        show_window_matrix_2_input()


def handle_pressing_matrix_check_symmetry_output_btn_done():
    clear_window_matrix_check_symmetry_output()
    show_window_menu_option_choice()


def handle_pressing_matrix_check_symmetry_output_btn_cancel():
    clear_window_matrix_check_symmetry_output()
    show_window_matrix_input()


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()  # создаём окно и привязываем его переменной root
root.title("Матричные операции")  # устанавливаем заголовок окна
root.geometry("1000x500")  # устанавливаем размеры окна
my_font=ctk.CTkFont(family="Roboto", size=20)  # задаём шрифт

# создаём виджеты для окон

# виджеты для главного окна - "menu_option_choice"
start_message_lbl = ctk.CTkLabel(master=root)
start_message_lbl.configure(text="Данная программа реализует матричные операции", font=my_font)
choose_option_message_lbl = ctk.CTkLabel(master=root)
choose_option_message_lbl.configure(text="Выберите опцию:", font=my_font)
options_choice_combobox = ctk.CTkComboBox(master=root)
options = ["Умножение матрицы на число", "Транспонирование матрицы", "Проверка матрицы на симметричность",
           "Сложение двух матриц", "Вычитание двух матриц",
           "Умножение двух матриц"]
options_choice_combobox.configure(values=options, justify="center", font=my_font)
options_choice_combobox.set("Умножение матрицы на число")
choose_option_btn_done = ctk.CTkButton(master=root)
choose_option_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_choose_option_btn_done)

# виджеты для окна ввода размеров матрицы - "matrix_size_input"
matrix_size_input_message_lbl = ctk.CTkLabel(master=root)
matrix_size_input_message_lbl.configure(text="Введите размеры матрицы:", font=my_font)
matrix_rows_input_message_lbl = ctk.CTkLabel(master=root)
matrix_rows_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_columns_input_message_lbl = ctk.CTkLabel(master=root)
matrix_columns_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_rows_input_entry = ctk.CTkEntry(master=root)
matrix_rows_input_entry.configure(font=my_font, justify="center")
matrix_columns_input_entry = ctk.CTkEntry(master=root)
matrix_columns_input_entry.configure(font=my_font, justify="center")
matrix_size_input_btn_done = ctk.CTkButton(master=root)
matrix_size_input_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_matrix_size_input_btn_done)
matrix_size_input_btn_cancel = ctk.CTkButton(master=root)
matrix_size_input_btn_cancel.configure(text="Назад", font=my_font, command=handle_pressing_matrix_size_input_btn_cancel)

# виджеты для окна ввода размеров 1-ой матрицы - "matrix_1_size_input"
matrix_1_size_input_message_lbl = ctk.CTkLabel(master=root)
matrix_1_size_input_message_lbl.configure(text="Введите размеры 1-ой матрицы:", font=my_font)
matrix_1_rows_input_message_lbl = ctk.CTkLabel(master=root)
matrix_1_rows_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_1_columns_input_message_lbl = ctk.CTkLabel(master=root)
matrix_1_columns_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_1_rows_input_entry = ctk.CTkEntry(master=root)
matrix_1_rows_input_entry.configure(font=my_font, justify="center")
matrix_1_columns_input_entry = ctk.CTkEntry(master=root)
matrix_1_columns_input_entry.configure(font=my_font, justify="center")
matrix_1_size_input_btn_done = ctk.CTkButton(master=root)
matrix_1_size_input_btn_done.configure(text="Готово", font=my_font,
                                       command=handle_pressing_matrix_1_size_input_btn_done)
matrix_1_size_input_btn_cancel = ctk.CTkButton(master=root)
matrix_1_size_input_btn_cancel.configure(text="Назад", font=my_font,
                                         command=handle_pressing_matrix_1_size_input_btn_cancel)

# виджеты для окна ввода размеров 2-ой матрицы - "matrix_2_size_input"
matrix_2_size_input_message_lbl = ctk.CTkLabel(master=root)
matrix_2_size_input_message_lbl.configure(text="Введите размеры 2-ой матрицы:", font=my_font)
matrix_2_rows_input_message_lbl = ctk.CTkLabel(master=root)
matrix_2_rows_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_2_columns_input_message_lbl = ctk.CTkLabel(master=root)
matrix_2_columns_input_message_lbl.configure(text="Количество строк:", font=my_font)
matrix_2_rows_input_entry = ctk.CTkEntry(master=root)
matrix_2_rows_input_entry.configure(font=my_font, justify="center")
matrix_2_columns_input_entry = ctk.CTkEntry(master=root)
matrix_2_columns_input_entry.configure(font=my_font, justify="center")
matrix_2_size_input_btn_done = ctk.CTkButton(master=root)
matrix_2_size_input_btn_done.configure(text="Готово", font=my_font,
                                       command=handle_pressing_matrix_2_size_input_btn_done)
matrix_2_size_input_btn_cancel = ctk.CTkButton(master=root)
matrix_2_size_input_btn_cancel.configure(text="Назад", font=my_font,
                                         command=handle_pressing_matrix_2_size_input_btn_cancel)

# виджеты для окна ввода матрицы - "matrix_input"
matrix_input_message_lbl = ctk.CTkLabel(master=root)
matrix_input_message_lbl.configure(text="Введите матрицу:", font=my_font)
matrix_input_textbox = ctk.CTkTextbox(master=root)
matrix_input_textbox.configure(font=my_font)
matrix_input_btn_done = ctk.CTkButton(master=root)
matrix_input_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_matrix_input_btn_done)
matrix_input_btn_cancel = ctk.CTkButton(master=root)
matrix_input_btn_cancel.configure(text="Назад", font=my_font, command=handle_pressing_matrix_input_btn_cancel)

# виджеты для окна ввода 1-ой матрицы - "matrix_1_input"
matrix_1_input_message_lbl = ctk.CTkLabel(master=root)
matrix_1_input_message_lbl.configure(text="Введите 1-ую матрицу:", font=my_font)
matrix_1_input_textbox = ctk.CTkTextbox(master=root)
matrix_1_input_textbox.configure(font=my_font)
matrix_1_input_btn_done = ctk.CTkButton(master=root)
matrix_1_input_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_matrix_1_input_btn_done)
matrix_1_input_btn_cancel = ctk.CTkButton(master=root)
matrix_1_input_btn_cancel.configure(text="Назад", font=my_font, command=handle_pressing_matrix_1_input_btn_cancel)

# виджеты для окна ввода 2-ой матрицы - "matrix_2_input"
matrix_2_input_message_lbl = ctk.CTkLabel(master=root)
matrix_2_input_message_lbl.configure(text="Введите 2-ую матрицу:", font=my_font)
matrix_2_input_textbox = ctk.CTkTextbox(master=root)
matrix_2_input_textbox.configure(font=my_font)
matrix_2_input_btn_done = ctk.CTkButton(master=root)
matrix_2_input_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_matrix_2_input_btn_done)
matrix_2_input_btn_cancel = ctk.CTkButton(master=root)
matrix_2_input_btn_cancel.configure(text="Назад", font=my_font, command=handle_pressing_matrix_2_input_btn_cancel)

# виджеты для окна ввода числа - "number_input"
number_input_message_lbl = ctk.CTkLabel(master=root)
number_input_message_lbl.configure(text="Введите число:", font=my_font)
number_input_entry = ctk.CTkEntry(master=root)
number_input_entry.configure(font=my_font, justify="center")
number_input_btn_done = ctk.CTkButton(master=root)
number_input_btn_done.configure(text="Готово", font=my_font, command=handle_pressing_number_input_btn_done)
number_input_btn_cancel = ctk.CTkButton(master=root)
number_input_btn_cancel.configure(text="Назад", font=my_font, command=handle_pressing_number_input_btn_cancel)

# виджеты для окна вывода итоговой матрицы - "matrix_result_output"
matrix_result_output_message_lbl = ctk.CTkLabel(master=root)
matrix_result_output_message_lbl.configure(text="Итоговая матрица:", font=my_font)
matrix_result_output_textbox = ctk.CTkTextbox(master=root)
matrix_result_output_textbox.configure(font=my_font)
matrix_result_output_btn_done = ctk.CTkButton(master=root)
matrix_result_output_btn_done.configure(text="Готово", font=my_font,
                                        command=handle_pressing_matrix_result_output_btn_done)
matrix_result_output_btn_cancel = ctk.CTkButton(master=root)
matrix_result_output_btn_cancel.configure(text="Назад", font=my_font,
                                          command=handle_pressing_matrix_result_output_btn_cancel)

# виджеты для окна вывода проверки матрицы на симметричность - "matrix_check_symmetry_output"
matrix_check_symmetry_output_message_lbl = ctk.CTkLabel(master=root)
matrix_check_symmetry_output_message_lbl.configure(text="Проверка на симметричность:", font=my_font)
matrix_check_symmetry_output_entry = ctk.CTkEntry(master=root)
matrix_check_symmetry_output_entry.configure(font=my_font, justify="center")
matrix_check_symmetry_output_btn_done = ctk.CTkButton(master=root)
matrix_check_symmetry_output_btn_done.configure(text="Готово", font=my_font,
                                                command=handle_pressing_matrix_check_symmetry_output_btn_done)
matrix_check_symmetry_output_btn_cancel = ctk.CTkButton(master=root)
matrix_check_symmetry_output_btn_cancel.configure(text="Назад", font=my_font,
                                                  command=handle_pressing_matrix_check_symmetry_output_btn_cancel)

# глобальные переменные, в которых будем хранить данные (изначально присвоим None, чтобы создать переменные)

flag_option = None  # хранит название опции, которую выбрали; нужна, чтобы понять, как переключаться между окнами
# например, мы в окне "matrix_1_input", понятно, что при нажатии на кнопку matrix_1_input_btn_done мы однозначно
# перейдём в окно "matrix_2_size_input", а при нажатии на кнопку matrix_1_input_btn_cancel мы однозначно перейдём в окно
# "matrix_1_size_input";
# теперь представим, что мы в окне "matrix_input", при нажатии на кнопку matrix_input_byn_done мы перейдём в одно из
# трёх окон: "number_input", "matrix_result_output", "matrix_check_symmetry_output". Выбор окна засит от выбора опции
# в самом начале. Поэтому нужна переменная-флаг, которая будет хранить выбор опции.

number_data = None  # сохраняем данные о введенном от пользователя из поля Entry числе
matrix_rows_data, matrix_columns_data, matrix_data = None, None, None  # сохраняем данные о матрице,
# если выбраны первые три опции
# сохраняем данные о двух матрицах, если выбраны последние три опции
matrix_1_rows_data, matrix_1_columns_data, matrix_1_data = None, None, None
matrix_2_rows_data, matrix_2_columns_data, matrix_2_data = None, None, None
# важный момент: когда считываем что-то от пользователя из полей Entry или TextBox, это считывается в типе данных str,
# поэтому переменные названы с постфиксом data

show_window_menu_option_choice()  # отрисовываем стартовое окно перед запуском программы

root.mainloop()  # запускаем главный цикл программы, теперь будут обрабатываться события при нажатии на кнопки
# с помощью функций-обработчиков событий (handler)
