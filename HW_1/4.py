"""
Сложность: n * log(n)
Алгоритм вначале сортирует список методом "разделяй и властвуй".
После чего формирует массив пар чисел с наименьшей разницей,
сравнивая только рядом стоящие числа, потому что их разница будет наименьшая благодаря сортировке.
Это уменьшает сложность программы.
На ответ программа возвращает массив из пар чисел.
"""


def merge(arr1, arr2):                      # функция, сортирующая два списка, полуценных из функции merge_sort
    i, j = 0, 0                             # индексы начала двух списков
    res = []
    while i != len(arr1) or j != len(arr2): # цикл повторяется, пока индекс не будет равен длине списка
        if i == len(arr1):
            res.append(arr2[j])             # если индекс одного списка равен длине - добавляеn элемент из второго списка
            j += 1                          # увеличение индекса
        elif j == len(arr2):
            res.append(arr1[i])             # аналогично предыдущему добавляет элемент из первого списка
            i += 1                          # увеличение индекса
        else:
            if arr1[i] < arr2[j]:           # сравнение элементов списка
                res.append(arr1[i])         # добавление меньшего элемента
                i += 1                      # увеличение индекса
            else:
                res.append(arr2[j])         # аналогично предыдущему добавление меньшего элемента
                j += 1
    return res                              # возвращает сортированный список из двух входных


def merge_sort(arr):                        # функция деления списка на два равных в рекурсии
    n = len(arr)//2                         # определение опорного элемента
    if len(arr) == 1:                       # проверка окончания списка
        return arr
    arr_1 = merge_sort(arr[:n])             # деление первой части списка в рекурсии
    arr_2 = merge_sort(arr[n:])             # деление второй части списка в рекурсии
    return merge(arr_1, arr_2)              # вызов функции сортировки


def minimumAbsDifference(arr):              #
    arr = merge_sort(arr)                   # сортировка списка
    min_diff = 999999999                    # определение начатьной минимальной разницы
    res = []
    for i in range(0, len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])     # определение текущей разницы с использованием модуля
        if min_diff > diff:                 # сравнивание текущей и минимальной разницы
            min_diff = diff                 # если текущая разница меньше, то она становится меньшей разницей
            res = [[arr[i], arr[i + 1]]]    # запись пары чисел с наименьшей разницей
        elif min_diff == diff:              # сравнивание текущей и минимальной разницы
            res.append([arr[i], arr[i +1]]) # добавление пары чисел с разницей, равной минимальной
    return res
