"""
Сложность: O(n)
Алгоритм производит деление входящего числа на 2 до того момента,
пока число положительное. При каждом делении увеличивается счётчик.
На ответ программа возвращает количество шагов деления.
"""


def numberOfSteps(num):
    count = 0               # счётчик количества делений
    while num > 0:          # делим на 2 пока num положительное
        if num % 2 != 0:    # проверка на чётность
            num -= 1        # при нечётном отнимает 1
            count += 1      # добавление шага
        else:
            num = num / 2   # при четном num делит на 2
            count += 1      # добавление шага
    return count
