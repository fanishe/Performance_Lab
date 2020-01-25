import random
import math

def generate_file(file, start = 1, end = 100):
    """генерирует файл с числами"""

    with open(file,'w',encoding = 'utf-8') as f:
       for i in range(int(start), int(end)):
           i = random.randint(int(start), int(end))
           f.write(f'{i}\n')

def create_list_form_txt(file = 'input.txt'):
    """ Необходимо выести название файла, по умолчанию input.txt"""
    try:
        with open(file,'r', encoding = 'utf-8') as f:
            some_list = []
            for line in f:
                some_list.append(int(line))
        return some_list

    except FileNotFoundError:
        generate_file(file)
    
def percentile(list, percent = 90):

    result = (len(list) * percent) / 100

    return sorted(list)[ math.floor(result) ]


def mediana(list):
    length = len(list)
    s_list = sorted(list)
    middle = length // 2

    if length % 2 == 0:
        return 0.5 * ( s_list[middle] + s_list[middle - 1] )
    else:
        return s_list[middle]

def main():
    # name_file = input('Enter filename\n')
    name_file = 'input.txt'
    data_list = create_list_form_txt(name_file)
    if not data_list:
        data_list = create_list_form_txt(name_file)
    print(percentile(data_list))
    print(mediana(data_list))
    print(min(data_list))
    print(max(data_list))



if __name__ == '__main__':
    main()
