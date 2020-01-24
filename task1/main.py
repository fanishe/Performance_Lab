import random
import math

def generate_file(file, start = 1, end = 100):
    """генерирует файл с числами"""

    with open(file,'w',encoding = 'utf-8') as f:
       for i in range(int(start), int(end)):
           i = random.randint(int(start), int(end))
           f.write(f'{i}\n')

def create_list_form_txt(file = 'input.txt'):
    """ Необюходимо ввыести название файла, по умолчанию input.txt"""
    try:
        with open(file,'r', encoding = 'utf-8') as f:
            some_list = []
            for line in f:
                some_list.append(int(line))
        return some_list

    except FileNotFoundError:
        generate_file(file)
    
def percentile(list, percent = 90):
    return sorted(list)[math.floor((len(list) * 90) / 100) ]



if __name__ == '__main__':
    name_file = input('Enter filename\n')
    data_list = create_list_form_txt(name_file)
    if not data_list:
        data_list = create_list_form_txt(name_file)
    print(percentile(data_list))