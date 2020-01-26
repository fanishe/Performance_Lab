"""
В магазине 5 касс, в каждый момент времени к кассе стоит очередь некоторой длины.

Каждые 30 минут измеряется средняя длина очереди в каждую кассу (число с плавающей запятой)
и для каждой кассы это значение записывается в соответствующий ей файл (всего 5 файлов).

Каждое значение заканчивается символом новой строки.
Магазин работает 8 часов в день.
Рассматривается только один день.

На момент запуска приложения все значения уже находятся в файлах.
Написать программу, которая по данным замеров определяет интервал времени, когда в магазине
было наибольшее количество посетителей за день.

Аргумент программы - путь к каталогу с файлами.
В каталоге будут 5 файлов: Cash1.txt, Cash2.txt ... Cash5.txt (Регистр имени важен!).


Пример одного из файлов:
1
1.2
1.3
1.34
1.5
1.9
1.7
1.832

Выведите номер интервала, в котором было наибольшее число посетителей в очередях магазина
на всех кассах.

Первый интервал идет под номером 1, последний под номером 16.
В случае обнаружения нескольких интервалов следует выводить первый из них.
"""
import random
import os
def generate_file(file, start = 1, end = 17):
    """генерирует файл с числами"""

    with open(file,'w', encoding = 'utf-8') as f:
       for i in range(int(start), int(end)):
           i = random.uniform(int(start), 10)

           # b = random.uniform(0, 1)
           f.write(f'{round(i, 3)}\n')
# generate_file('cashes/Cash5.txt')

# TODO
#[v] Сделать списки из файлов
# Найти в каждом из них макс значение
    # пройтись по каждому словарю одновременно
    # сохранить все числа в переменную
    # след ряд
    # если след ряд больше пред
        # сохранить
    # если нет
        # продолжить итерацию
    # вернуть переменную

# Вычленить интервал с макс значениями

def make_lists(path = 'C:\\Users\\PC\\Documents\\GitHub\\Performance_Lab\\task3\\cashes'):
    files = os.listdir(path)
    # print(files)
    # ['Cash1.txt', 'Cash2.txt', 'Cash3.txt', 'Cash4.txt', 'Cash5.txt']
    cash_dict = {}

    for file in files:
        with open(f'{path}/{file}','r', encoding = 'utf-8') as f:
            some_list = []
            for line in f:
                some_list.append(float(line))
            cash_dict[f'{file[:5].lower()}'] = some_list
    return cash_dict

def search_max(dicts):
    for dict in dicts:
        max_val = max(dicts[dict])
        interval = dicts[dict].index(max_val)
        print(f'max = {max_val} index =  {interval}')
    




if __name__ == '__main__':
    # main()
    dir = os.path.abspath(os.curdir)
    cash_dict = make_lists(f'{dir}/cashes')
    search_max(cash_dict)
