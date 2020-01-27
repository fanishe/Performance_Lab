import random
import os
import sys

var = sys.argv[1:]


def generate_file(file, start = 1, end = 17):
    """генерирует файл с числами"""

    with open(file,'w', encoding = 'utf-8') as f:
       for i in range(int(start), int(end)):
           i = random.uniform(int(start), 10)
           f.write(f'{round(i, 3)}\n')

# for i in range(1, 6):
    # print(f' Generate cashes/Cash{i}.txt')
    # generate_file(f'cashes/Cash{i}.txt')


def make_lists(way):
    """ Принимает путь к папке и делает и файлов словарь """
    files = os.listdir(way)
    # ['Cash1.txt', 'Cash2.txt', 'Cash3.txt', 'Cash4.txt', 'Cash5.txt']
    cash_dict = {}

    for file in files:
       dir =  os.path.join(f'{way}', f'{file}')
       with open(dir, encoding = 'utf-8') as f:
            some_list = []
            for line in f:
                some_list.append(float(line))
            cash_dict[f'{file[:5].lower()}'] = some_list
    return cash_dict

def search_max(dicts):
    """ Принимает созданный словарь и вычисляет максимальное кол-во посетителей"""
    sum1 = [] 
    for num in range(0, 16):
        # как мне показалось самый простой вариант, это сложить всех людей на кассах
        # и найти максимальное число 
        # если я  правильно понял задание, то надо вернуть индекс максимального числа
        sum1.append(dicts['cash1'][num] + dicts['cash2'][num] + dicts['cash3'][num] + dicts['cash4'][num] + dicts['cash5'][num])
    max_val = max(sum1)
    interval = sum1.index(max_val)
    # print(f'max = {max_val} index =  {interval}')
    return f'{interval}\n'




def main(way_to_dir):
    cash_dict = make_lists(f'{way_to_dir}')
    index =  search_max(cash_dict)
    print(index)


if __name__ == '__main__':
    main(var[0])
