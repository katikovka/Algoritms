"""
Сложность: O(n)
Алгоритм раскрывает скобки и ищет пары закрывающихся скобок с донном списке.
"""

def removeOuterParentheses(s):
    count = 0                                   # счётчик количества пары скобок
    res = []                                    # список, в который будет заносится результат
    for i in range(0, len(s)):                  # цикл проходит по строке s
        flag = False                            # индикатор для обозначения открывающейся скобки (False - открытв, True - закрыта)
        if s[i] == "(":
            count += 1                          # если скобка открыта, увеличивает счётчик
        elif s[i] == ")":
            count -= 1                          # если скобка закрыта, уменьшает счётчик
            flag = True
        if count != 0 and (count != 1 or flag): # добавляет в список res, если на счётчике нет открытой скобки и это не последняя закрвающаяся скобка
            res.append(s[i])
    return "".join(res)                         # перевод списка в строку для ответа
