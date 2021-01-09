"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def my_func():
    elem = max(set(array), key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(f'Функция func_1() {timeit.timeit("func_1()", setup="from __main__ import func_1", number=10000)}')
print(f'Функция func_2() {timeit.timeit("func_2()", setup="from __main__ import func_2", number=10000)}')
print(f'Функция my_func() {timeit.timeit("my_func()", setup="from __main__ import my_func", number=10000)}')
''' Результаты профилирования 
Функция func_1() 0.012565581997478148
Функция func_2() 0.015171304999967106
Функция my_func() 0.010198818999924697

По результатам профилирования моя функция быстрей за счет использования функции max с параметром key и 
перевода во множество для отсечения дублей
'''
print(func_1())
print(func_2())
print(my_func())
