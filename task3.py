"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile
import time
import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        time.sleep(0.2)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        time.sleep(0.2)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    time.sleep(0.2)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    num = 12345678905675757575675
    result_revers = revers(num)
    result_revers2 = revers_2(num)
    result_revers3 = revers_3(num)


''' Замеряем производительность через cProfile
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.416    9.416 <string>:1(<module>)
     24/1    0.001    0.000    4.608    4.608 task_3.py:18(revers)
        1    0.000    0.000    4.607    4.607 task_3.py:29(revers_2)
        1    0.000    0.000    0.200    0.200 task_3.py:38(revers_3)
        1    0.000    0.000    9.416    9.416 task_3.py:45(main)
        1    0.000    0.000    9.416    9.416 {built-in method builtins.exec}
       47    9.415    0.200    9.415    0.200 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Результат ожидаемый Функция revers это рекурсивная функция самая медленная так и должно быть
она накапливает вызовы время исполнения 4.608

Функция revers_2 цикл с пред условием чуть быстрей потому что рекурсивных вызовов не.
Но всетаки есть итерации цикла. Эмуляция рекурсии время исполнения 4.607

Функция revers_3 самая быстрая здесь просто реверсируется список штатными методами.
Нет не рекурсии не итераций в цикле. Время испонения 0.200
'''

cProfile.run('main()')

''' Замеряем производительность с помощью timeit'''
num = 12

print(f'Функция revers(num) {timeit.timeit("revers(num)", setup="from __main__ import revers, num", number=10)}')
print(f'Функция revers_2(num) {timeit.timeit("revers_2(num)", setup="from __main__ import revers_2, num", number=10)}')
print(f'Функция revers_3(num) {timeit.timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=10)}')

''' Результаты после замера по timeit подтвердили преыдущий результат 
Функция revers(num) 4.006537515000673
Функция revers_2(num) 4.006396142001904
Функция revers_3(num) 2.0035113930025545

'''
